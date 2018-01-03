import sys
import re

padrao = sys.argv[1]
texto = sys.argv[2]
match = re.match(padrao,texto)

if match:
    template = "'{}' contem padrao '{}'"
else:       
    template = "'{}' nao contem padrao '{}'"

print(template.format(texto,padrao))

