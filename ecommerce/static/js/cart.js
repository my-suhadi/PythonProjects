const updateBtn = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;

        console.log('product-id: ', productId, 'action: ', action);
        console.log('user: ', user);

        if (user === 'AnonymousUser') {
            console.log('Unauthenticated User');
        } else {
            updateUserOrder(productId, action);
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('user send a data');

    const url = 'update-item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data: ', data);
            location.reload();
        })
}