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

var container = document.getElementById('watch_big');

function changeColor(src){
    container.firstElementChild.setAttribute('src', src);   
}

var img_container = document.getElementById('img_list')
 var imgs = img_container.querySelectorAll('span');

 imgs.forEach(element=>{
    element.addEventListener('click', ()=>{
        removeBorder();
        element.style.borderColor  = '#7B7B75';
    })
 })

function removeBorder(){
    imgs.forEach(element=>{
        element.style.borderColor = '#DFDFD6'
    })
}




    star_container = document.getElementById('stars_container'); 

    makeStars(star_container, rating, starfull, starhalf, starnone)

function makeStars(star_container, rating,  starfull, starhalf, starnone){
    var i;
           
    for(i=0;i<5;i++){
        var span = document.createElement('span');
        var img = document.createElement('img');
        if(rating>=1){
            img.src = starfull;
             console.log(rating)
            --rating;
        }       
        else if(rating>=0.5){
            img.src = starhalf;
            console.log(rating);
            rating-=0.5;
        }  
        else{
            img.src = starnone;
            console.log(rating);
        }
        
        span.appendChild(img);
        star_container.appendChild(span);
    }
   
}

