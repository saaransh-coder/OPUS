const balance = document.getElementById('balance')

const money_plus = document.getElementById('money-plus')

const money_minus = document.getElementById('money-minus')

const list = document.getElementById('list')

const form = document.getElementById('form')

const text = document.getElementById('text')

const amount = document.getElementById('amount')


let transactions = []

async function getTransactions() {
    const res = await fetch('api/transactions/')

    const data = await res.json()
    console.log("Data loaded :", data)

    transactions = data

    init()
}

function addTransactionDom(transaction) {
    const symbol = transaction.amount < 0 ? '-' : '+'
    const item = document.createElement('li')

    item.classList.add(transaction.amount < 0 ? 'minus' : 'plus')

    item.innerHTML = `${transaction.text} <span>${symbol} ${Math.abs(transaction.amount)}</sapn>
    <button class="delete-btn" onclick="removeTransaction(${transaction.id})">X</button>`

    list.appendChild(item)
}


function updateValues() {
    const amount = transactions.map(transactions => parseFloat(transactions.amount))

    const total = amount.reduce((a, item) => (a += item), 0).toFixed(2)

    const income = amount.filter(item => item > 0).reduce((a, item) => (a += item), 0).toFixed(2)

    const expense = amount.filter(item => item < 0).reduce((a, item) => (a += item), 0).toFixed(2)

    balance.innerText = `${total}`

    money_plus.innerText = `+${income}`

    money_minus.innerText = `-${expense}`
}

async function addTransaction(e) {
    e.preventDefault()

    if (text.value.trim() === '' || amount.value.trim() === '') {
        alert("Enter the text")
        return
    }

    const transactionData = {
        text: text.value,
        amount: +amount.value
    }

    console.log("Sending data:", transactionData);

    const res = await fetch('/api/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(transactionData)
    })


    const data = await res.json()

    if (!res.ok) {
        alert(`Server Error: ${responseData.error}`);
        console.error("Server Error:", responseData);
        return;
    }


    transactions.push(data)
    addTransactionDom(data)
    updateValues()

    text.value = ""
    amount.value = ""
}


async function removeTransaction(id) {
    await fetch(`/api/delte/${id}/`, {
        method: 'DELETE'
    })

    transactions = transactions.filter(transactions => transactions.id !== id)

    init()
}


function init() {
    list.innerHTML = ''

    transactions.forEach(addTransactionDom)
    updateValues()
}

getTransactions()

form.addEventListener('submit', addTransaction)
