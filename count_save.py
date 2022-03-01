while True:
    site=input('Site: ')
    if site == 'finish':
        break
    login=input('Login: ')
    senha=input('Senha: ')
    note=open(f'run\\{site}.txt','w')
    note.write(f'{login}\n{senha}')
    note.close()
