

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

//sortbox dropdown
let arrow = document.getElementById('arrow');
let sortbox = document.getElementById('dropoptions');
arrow.addEventListener('click', ()=>{
    if(arrow.getAttribute('src')=== down_arrow){
        arrow.setAttribute('src',up_arrow)
        sortbox.style.display = 'block';
    }
    else{
        arrow.setAttribute('src', down_arrow);
        sortbox.style.display = 'none';
    }
});

let options = sortbox.children;
let current_option = document.getElementById('option')
let i;
for(i=0;i<options.length;i++){
    options[i].addEventListener('click',(e)=>{
        var choice = e.target.innerText;
        current_option.innerText = choice;
        arrow.setAttribute('src', down_arrow);
        sortbox.style.display = 'none';
    })
}


var Arrows =  document.querySelectorAll('.arrow_icon');

//filter dropdown
Arrows.forEach(element =>{
    element.addEventListener('click',()=>{
        console.log(element.firstChild.getAttribute('src'))
        if(element.firstChild.getAttribute('src') === up_arrow){
            element.firstChild.setAttribute('src', down_arrow)
            element.parentElement.nextElementSibling.style.display = 'none';
        }
        else{
            element.firstChild.src = up_arrow;   
            element.parentElement.nextElementSibling.style.display = 'block';
        }
    });
})


var div = document.getElementById('choices')
function createNode(txt){
    div.style.display = 'flex';
    var text = document.createTextNode(txt);
    var span = document.createElement('span');
    var span_img = document.createElement('span');
    span_img.style.cursor = 'pointer';
    span_img.className = 'close';
    var div2 = document.createElement('div');
    div2.className = 'filteractive';
    var img = document.createElement('img');
    img.setAttribute('src', close);
    span_img.appendChild(img);
    span.appendChild(text);
    div2.appendChild(span);
    div2.appendChild(span_img);
    div.appendChild(div2)

    span_img.addEventListener('click',()=>{
        span_img.parentElement.remove();
        uncheck(txt);
    })
}


let labels = document.querySelectorAll('label');

labels.forEach(element =>{
    element.addEventListener('input', ()=>{
        text = element.lastChild.innerText;
        if(element.firstChild.checked){
            document.getElementById('clear').style.display = 'inline'
            createNode(text);
        }
        else{
            var active_filters =  div.querySelectorAll('.filteractive');
            active_filters.forEach(filter =>{
                if(filter.innerText === text)
                    filter.remove();

                if(!div.firstElementChild.nextElementSibling)
                    clearAll();
            })
        }


    });
});


function uncheck(txt){
    labels.forEach(element =>{
        var text = element.lastChild.innerText;
        if(txt === text){
            element.firstChild.checked = false;
        }
        if(!div.firstElementChild.nextElementSibling)
            clearAll();
    });
}


function clearAll(){
    var active_filters =  div.querySelectorAll('.filteractive');

    active_filters.forEach(element =>{
       element.remove();
    });
    div.style.display = 'none';
    labels.forEach(element =>{
        element.firstChild.checked = false;
    })
}


var filter_img = document.getElementById('filter_img');
var filters = document.getElementById('filters')
if(screen.width > 1023)
    filter_img.disabled = true;
filter_img.addEventListener('click',()=>{
    filters.style.display === 'block' ? filters.style.display = 'none': filters.style.display = 'block';
})

var like = document.querySelectorAll('.like');

like.forEach(element=>{
    element.addEventListener('click',()=>{
        element.firstChild.getAttribute('src') === like_inactive ? element.firstChild.setAttribute('src', like_active) : element.firstChild.setAttribute('src', like_inactive)
    })
})


// console.log(wishlist[1])