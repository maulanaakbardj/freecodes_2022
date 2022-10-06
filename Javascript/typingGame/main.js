const RANDOM_QUOTE_API_URL='http://api.quotable.io/random';

let quoteDisplayElement= document.getElementById('quoteDisplay');
let quoteInputElement= document.getElementById('quoteInput');
let timerElement= document.getElementById('timer');
let completed= true;


quoteInputElement.addEventListener('input',()=>{
    const arrayQuote=quoteDisplayElement.querySelectorAll('span');
    const arrayValue= quoteInputElement.value.split('');
    arrayQuote.forEach((characterspan,index)=>{
        const character = arrayValue[index];
        // console.log('Character is',character);
        // console.log("Characterspan is",characterspan);
        
        if (character=== characterspan.innerText){
            characterspan.classList.add('correct');
            characterspan.classList.remove('incorrect');
            completed=true
        }
        else if (character==null){
            completed= false;
            characterspan.classList.remove('incorrect')
            characterspan.classList.remove('correct')
            
        }
        else{
            completed=false;

            characterspan.classList.add('incorrect');
            characterspan.classList.remove('correct');
            
        }
    })
    if (completed){
        const sameButton=document.getElementById('play_again')
        const nextButton=document.getElementById('play_next')
        const buttons= document.getElementsByClassName('btn')
        for (let i=0;i <buttons.length;i++){
            buttons[i].style.display="block"
        }
        sameButton.addEventListener('click',()=>{
            quoteInputElement.value= null;
        });
       
        nextButton.addEventListener('click',()=>{
            renderNewQuote();
        });

    };
   
});

function getRandomQuote(){
    return fetch(RANDOM_QUOTE_API_URL)
    .then(response=>response.json())
    .then(data=>data.content);
}

// console.log(getRandomQuote())


async function renderNewQuote(){

    const quote= await getRandomQuote();
    quoteDisplayElement.innerText="";
    quote.split('').forEach(character => {
        const characterSpan= document.createElement('span');
        // characterSpan.classList.add('incorrect')
        // characterSpan.classList.add('correct')
        characterSpan.innerText= character
        quoteDisplayElement.appendChild(characterSpan)
        startTimer();
        
    });
    quoteInputElement.value= null;
    // console.log(quote);
}

let startTime;
const startTimer= ()=>{
    timerElement.innerText=0;
    startTime= new Date();
   setInterval(() => {
       timerElement.innerText= getTimerTime()
       
   }, 1000);
}

function getTimerTime(){
    
    return Math.floor((new Date() - startTime)/1000)
}
renderNewQuote();