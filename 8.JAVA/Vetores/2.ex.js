const listaDeNumeros = [1, 2, 3, 4, 5, 6]

console.log('Listando todos os valores da lista: ')
console.log(listaDeNumeros)

console.log('\nFiltrando elementos pares: ')
const pares = listaDeNumeros.filter(numero => numero % 2 === 0)
console.log(pares)

console.log('\nFiltrando elementos ímpares: ')
const impares = listaDeNumeros.filter(numero => numero % 2 !== 0)
console.log(impares)