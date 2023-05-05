


let imagediv = document.querySelector('#imagediv')
let ratname = document.querySelector('#ratname')
let rattext = document.querySelector('#rattext')
let changename = document.querySelector('#changename')

changename.addEventListener("click", e => {
    rattext.innerHTML =`This rat is called ${ratname.value}! You can rename them below`
    ratname.value = ""
})

let sadbutton = document.querySelector("#sadbutton")
let happybutton = document.querySelector("#happybutton")
let neutralbutton = document.querySelector("#neutralbutton")
let sleepybutton = document.querySelector("#sleepybutton")
let ratbox = document.querySelector("#ratbox")
let takecheesebutton = document.querySelector("#takecheesebutton")


let cheese0 = document.querySelector('#cheese0')
let cheese1 = document.querySelector('#cheese1')

let amountOfCheese = 2
let numberOfNaps = 0
let numberOfStories = 0
let numberOfSmiles = 0

changename.addEventListener("click", e => {
    rattext.innerHTML =`This rat is called ${ratname.value}! You can rename them below`
    ratname.value = ""
})

sadbutton.addEventListener("click", e => {
    console.log("sad button clicked!")
    ratbox.classList.toggle('sad')
    imagediv.innerHTML = `<img src="images/sad.png" />`
    numberOfStories+=1
})
happybutton.addEventListener("click", e => {
    console.log("happy button clicked!")
    ratbox.classList.toggle('happy')
    imagediv.innerHTML = `<img src="images/happy.png" />`
    numberOfSmiles += 1

})
neutralbutton.addEventListener("click", e => {
    console.log("neutral button clicked!")
    ratbox.classList.toggle('neutral')
    imagediv.innerHTML = `<img src="images/neutral.png" />`
})
sleepybutton.addEventListener("click", e => {
    console.log("sleepy button clicked!")
    imagediv.innerHTML = `<img src="images/sleeping.png" />`
    numberOfNaps +=1
})
takecheesebutton.addEventListener("click",e => {
    ratbox.classList.toggle('mad')
    console.log("you took their cheese!! >:(")
    imagediv.innerHTML = `<img src="images/mad.png" />`
    if(amountOfCheese == 2 ){
        cheese0.innerHTML=``
        amountOfCheese = 1
    } else if(amountOfCheese == 1){
        amountOfCheese = 0
        cheese1.innerHTML=``
        takecheesebutton.innerHTML=``
    }
})