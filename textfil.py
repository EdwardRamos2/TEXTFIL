#!/usr/bin/env python3
import sys, os, subprocess, platform
print('.     .       .  .   . .   .   . .    +  .')
print('  .     .  :     .    .. :. .___---------___.')
print('       .  .   .    .  :.:. _ .^ .^ ^.  . . :_. .')
print('    .  :       .  .  .:../:            . .^  :.:\.')
print('        .   . ::  . :.:/: .   .    .        . . .:\.')
print(' .  :    .     . _ :::/:               .  ^ .  . .:\/')
print('  .. . .   . - : :.:./.                        .  .:\/')
print('  .      .     . :..|:                    .  .  ^. .:|')
print('    .       . : : ..||        .                . . !:|')
print('  .     . . . ::. ::\(                           . :)/')
print(' .   .     : . : .:.|. ######               #######::|')
print('  :.. .  :-  : .:  ::|.#######           ..########:|')
print(' .  .  .  ..  .  .. :\ ########          :######## :/')
print('  .        .+ :: : -.:\ ########       . ########.:/')
print('    .  .+   . . . . :.:\. #######       #######..:/')
print('      :: . . . . ::.:..:.\           .   .   ..:/')
print('   .   .   .  .. :  -::::.\.       | |     . .:/')
print('      .  :  .  .  .-:.":.::.\             ..:/')
print(' .      -.   . . . .: .:::.:.\.           .:/')
print('.   .   .  :      : ....::_:..:\   ___.  :/')
print('   .   .  .   .:. .. .  .: :.:.:\       :/')
print('     +   .   .   : . ::. :.:. .:.|\  .:/|')
print('     .         +   .  .  ...:: ..|  --.:|')
print('.      . . .   .  .  . ... :..:.."(  ..)"')
print(' .   .       .      :  .   .: ::/  .  .::\.')
def inter_graf(linha_repet):
    print(linha_repet)
inter_graf('_' *90);print('VERSION: 1.0 (((TEXTFIL)))       By: Edward Ramos        Date: 01032017')
print('OS',platform.system(),platform.machine(),platform.node(),platform.platform());inter_graf('_' *90)
print('OPTION   |                          DESCRIPTION(filters)\n')
print('  1      -    cat  +Usado para mostrar o conteudo de arquivos, do inicio ao final: ')


opcao = input('Digite uma opcao: ')

if opcao == '1':
    print('cat [opcoes] arquivo')
    print('onde opcoes')
    print('1 >>>   -n -> numera as linhas')
    print('2 >>>   -b -> exibe as linhas que nao estao em branco')
    print('3 >>>   -A -> mostra as quebra de linha')
    opcao2 = input('>>> ')
    if opcao2 == '1':
        arquivo = str(input('Nome do arquivo: '))
        print(arquivo)
        os.system('cat -n {0}'.format(arquivo))
        
