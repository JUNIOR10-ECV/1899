// Instalar: npm install readline-sync

// Limpar o terminal
console.clear()

const readline = require('readline-sync')

const idade = readline.questionInt('Digite sua idade: ')

if (idade < 16) { 
    console.log('Não pode votar.')
} else if (idade >=16 ) {
    console.log('Voto opicional.')
} else if (idade >18) {
    console.log('Voto oobrigatório.')
} else if(idade >65) {
    console.log('Não é obrigado a votar.')
} else{
    print ('Ordem e Progresso')
}