import io
import vcd
from vcd.reader import TokenKind

with open('dump.vcd', 'rb') as f:
  vcd_content = f.read()

tokens = vcd.reader.tokenize(io.BytesIO(vcd_content))

i = 0;
try:
  while True:
    token = next(tokens)
    if token.kind is TokenKind.VAR:
      print(f'{token.data.ref_str}')
      #print(f'{token.data.ref_str()} --> {token.data.id_code}')
#    if token.kind is TokenKind.CHANGE_TIME:
#      print(f'time change: {token.data}')
#    if token.kind is TokenKind.CHANGE_SCALAR:
#      print(f'clk value: {token.data.value}')
#    if token.kind is TokenKind.CHANGE_VECTOR:
#      print(f'a value: {token.data.value}')
    i = i + 1
except StopIteration:
  print(f'Done after {i} lines! ')



