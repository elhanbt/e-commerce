    
    var product_prices = document.querySelectorAll('.product_price');
    var discount_price = document.querySelectorAll('.discount_price');
    
    var total_price = document.getElementById('itemprice');
    const original_prices = [];
    const discount_prices = [];

    var sum1 = 0
    product_prices.forEach(function(element,index){
        // console.log(index)
        original_prices[index] = parseInt(element.innerHTML);
        sum1 = sum1 +  parseInt(element.innerHTML);
    });
    total_price.innerHTML =  sum1;

    var discount = document.getElementById('discount');
    sum2 = 0 
    discount_price.forEach(function(element,index){
        // console.log(element.innerHTML)
        discount_prices[index] = parseInt(element.innerHTML);
        sum2 = sum2 + parseInt(element.innerHTML);
    });
    discount.innerHTML = sum1 - sum2

    document.getElementById('total').innerHTML = 'Rs.'  + (parseInt(total_price.innerHTML) - parseInt(discount.innerHTML) + 49)

    console.log(discount_prices)
    

    function change(char, box){
        id = 'count_' + box;
        // console.log(id);
        var count = parseInt(document.getElementById(id).innerText);
        if(char == '-' && count>1){    
            count = count - 1;
        }
        else if(char == '+'){
            count= count + 1;
        }
        document.getElementById(id).innerText = count;

        id = 'product_price_' + box;
        document.getElementById(id).innerHTML = original_prices[box-1] * count
        
        var sum1 = 0
        product_prices.forEach(function(element,index){
            // console.log(index)
            sum1 = sum1 +  parseInt(element.innerHTML);
        });
        total_price.innerHTML =  sum1;

        id = "discount_price_" + box;
        document.getElementById(id).innerHTML = discount_prices[box-1] * count;

        sum2 = 0 
        discount_price.forEach(element=>{
            // console.log(element.innerHTML)
            sum2 = sum2 + parseInt(element.innerHTML);
        });
        discount.innerHTML = sum1 - sum2;

        document.getElementById('total').innerHTML = 'Rs.'  + (parseInt(total_price.innerHTML) - parseInt(discount.innerHTML) + 49)

    
    }
// console.log(original_prices)

    var drop = document.getElementById('dropdownwrapper');
    var dropdown1 = document.getElementById('drop1');
    var dropdown2 = document.getElementById('drop2');

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

drop.addEventListener('click', function(event){
    if(!dropdown2.contains(event.target)){
        drop.style.display = 'none';
    }
});
    
