
// dropdowns when the user profile name is clicked
var drop = document.getElementById('dropdownwrapper');
    var dropdown1 = document.getElementById('drop1');
    var dropdown2 = document.getElementById('drop2');

    var add_address = document.getElementById('add_address_modal');

function dropdown(box){
    drop.style.display = 'block';

    if(box === '2'){
        dropdown2 .style.display = "flex";
        dropdown1.style.display = "none";
     }
    
    else if(box === '1'){
        dropdown1.style.display = "block";
        dropdown2.style.display = "none";      
    }
}

// display modal for deleting address
var delete_button = document.querySelectorAll('.delete');
var delete_modal = document.getElementById('delete_modal')
console.log(delete_button)
delete_button.forEach(element =>{
    element.addEventListener('click', ()=>{
        drop.style.display = 'block'
        delete_modal.style.display = 'block';
    })
})

var container = document.getElementById('form_container');
var modals = document.querySelectorAll('.address_modal')

// removes all modals when clicked anywhere on screen
drop.addEventListener('click', function(event){
    if(!dropdown2.contains(event.target) && !add_address.contains(event.target) && !container.contains(event.target)){
        drop.style.display = 'none';
         add_address.style.display = 'none';
         dropdown1.style.display = "none";
        //  delete_modal.style.display = 'none';
         container.style.display = 'none';
         modals.forEach(element =>{
            element.style.display = 'none';
         });

    }
});

function closeModals(){
    drop.style.display = 'none';
    add_address.style.display = 'none';
    dropdown1.style.display = "none";
    // delete_modal.style.display = 'none';
    modals.forEach(element =>{
        element.style.display = 'none';
     });
}

// modal for adding address
function addAddress(){
    drop.style.display = 'block';
    add_address.style.display = 'block'
    
}


// validating phone number in form
const phone = document.getElementById('phone');
phone.addEventListener('input', function(e) {
    
    phone.value = phone.value.replace(/[^0-9]/g, '');

    var code = /^([0-9]{3})([0-9]{3})([0-9]{4})$/;
    var match = phone.value.match(code);
    if (match) {
       
        phone.value = `${match[1]}${match[2]}${match[3]}`;
    } 
});

// all fields are filled
var form = document.getElementById('form');
var input = form.querySelectorAll('input');
var radio = document.querySelectorAll('.radio');
input.forEach(element =>{
    element.addEventListener('input', validate);
});

function validate(){
    let isValid = true;
    var flag = -1;
    input.forEach(element =>{
        if(element.value.trim() === '')
            isValid = false;
    });

    if(phone.value.length < 10){
        isValid = false
    }

   

    if(!isValid){
        document.getElementById('save').disabled = true;
    }
    else{
        document.getElementById('save').disabled = false;
    }
}

