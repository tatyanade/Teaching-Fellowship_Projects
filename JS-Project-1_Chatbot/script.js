function errorMessage(){
    alert("You did not type a valid response. Please press 'Embark' to continue, or refresh your page to restart.")
}

function note(num){
    if (num === 1){
        return "\n \n Note: Please type in '1' to continue."
    } else {
        let message =  "\n \n Note: Please type in '1', "
        for (let i = 2; i <= num-1; i++){
            message+= "'" + i + "', "
        }
        message += "or '" + num + "' to continue."
        return message;
    }
    // '1', '2', or '3' to continue"
}

let hasKey = false;
let hasUsedKey = false;
let hasBeenToCastle = false;
let hasBeenToGhostTown = false;
let hadBeenToTown = false;
let hasSeenGhostFeatherMerchant = false;
let hasTalkedWithFeatherMerchant = false;
let hasFeather = false;
let hasBeenToHaberdashery = false;
let hasCloak = false;
let hasComeBackToCastle = false;
let hasBeenToCastleMoat = false;

//Landervillours
function startGame(){
    let choice = prompt("Welcome to the town of Vouderlais - a medieval town that primarily focuses on agriculture. The rats who live here spend their time cultivating several types of cheese that are well known throughout the realm. There are also several high-quality bushes with fine and lovely berries. most of the farms are on the outskirts of town, becoming smaller as they near the town square. In the center of town, there are many merchants selling trinkets and knickknacks, as well as shops and warehouses and workshops. Down a ways is the castle, where the mouse Bobouse is supposed to live, however as ou have never been to Vouderlais before, you cannot confirm any of these facts. \n \n \n You are currently in the town square. What do you with to do? \n \n 1. Look around the town square \n 2. Check out the farms \n 3. Go to the castle" + note(3))

    //User Chose to stay in the town square
    if (choice === "1"){
        atTownSquare()
    //user chose to go to castle
    } else if (choice === "2"){
        atFarms()
    //user chose to go to farms
    } else if (choice === "3"){
        headToCastle()
    //user didnt play correctly
    } else {errorMessage()}
}

function atTownSquare(){
    hasBeenToTown = true
    let message = ""

    if (hasBeenToCastle === false){
        message+= "You are in the town square! There are so many people to meet and things to buy and friends to make and food to eat and things to look at! You are thrilled. You look around and see a few shops of note: a haberdashery and a cheese emporium and even a feather merchant! \n \n \n What do you wish to do?"
    } else {
        if (hasBeenToGhostTown === false){
            message += "You are at the town square. You remember when you where last here it was bustling with people, all cheery and friendly. \n You don't know what happened but now it's completely empty. \n Not even the wind is blowing. You don't like this at all. \n \n \n What do you want to do?"
            hasBeenToGhostTown = true
        } else {
            message+= "The town is still empty. You remember what it was like when it was lively and crowded, but not it is silent and still. \n \n \n How do you wish to procede?"
        }
    }
    message += "\n \n 1. Go to the Haberdashery \n 2. Go to the cheese emporium \n 3. Go to the feather merchant's stall \n 4. Head towards the farms \n 5. Head towards the castle"

    let choice = prompt(message + note(5))

    if (choice === "1"){
        atHaberdashery()
    } else if (choice === "2") {
        atCheeseEmporium()
    } else if (choice === "3"){
        atFeatherMerchant()
    } else if (choice === "4"){
        atFarms()
    } else if (choice === "5"){
        headToCastle()
    } else { errorMessage() }
}

function atHaberdashery(){
    if(hasBeenToGhostTown == true){
        let choice = prompt("You enter the haberdashery, but theres no one here - the shop is empty. \n \n \n What do you do? \n \n 1. Head back to the town" + note(1))
        if (choice == 1 ){
            atTownSquare()
        }
    } else {
        if(hasBeenToHaberdashery === false){
            hasBeenToHaberdashery = true;
            let message = "As soon as you step into the haberdashery, a magnificent looking rat with freckled light orange fur steps towards you \n 'Oh hello! I haven't seen your face around here before! This must be your first time in town! My name is Bandine.' \n Bandine pauses for a moment, lost in contemplation as they look you over \n 'Ah... I have the perfect thing. We just got this coat in last week, It's a deep brown velvet and has a nice subtle gold trim on it. "
            if (hasFeather === true){
                message += "I think it would look very nice with that feather you are wearing!"
            }
            message += " What do you say, are you interested? \n \n \n What do you do? \n \n \n 1. Purchase the cloak and return to the town square \n 2. Politely decline and head back to town"
            let choice = prompt(message + note(2))
            if (choice === "1"){
                hasCloak = true
            }
            if (choice === "1" || choice==="2"){
                atTownSquare()
            } else { errorMessage() }
        } else { 
            if (hasCloak == false){
                let choice = prompt("You go back into the haberdashery. It is a bit busy, and Bandine is helping another rat choose which socks to buy. As soon as they see you, Bandine pauses their conversation to let you know that if you changed your mind about the cloak it's still available. \n \n \n What do you do? \n \n 1. Purchase the cloak and leave the haberdashery \n 2. Return to the town square" + note(2))
                if (choice === "1") {
                    hasCloak = true
                    atTownSquare()
                } else if (choice === "2"){
                    atTownSquare()
                } else { errorMessage() }
            } else {
                let choice = prompt("You return to the haberdashery but it is much busier than last time, buzzing with customers. Bandine is occupied talking to 12 different rats, each trying to decide between a new coat, a new hat, or twelve new silk scarves.\n \n \n What are you going to do next? \n \n 1. Head back to town" + note(1))
                if (choice === "1") {
                    atTownSquare()
                } else { errorMessage() }
            }
        }
    }
}

function atCheeseEmporium(){
    if(hasBeenToGhostTown == true){
        let choice = prompt("You enter the cheese emporium, hopeing for a morsel or cube to snack on, but there is nothing. Only the memory of the hint of the implication of the smell of cheese, and it lingers on your nose. \n \n \n What do you do? \n \n 1. Head back to the town" + note(1))
        if (choice == 1 ){
            atTownSquare()
        } else { errorMessage() }
    } else {
        let choice = prompt("You enter the enter emporium. There is a very nice rat there named Marmalade. They greet you with a courteous smile and ask if they can help you with anything. \n  'Hello! Would you like to buy anything today?' says Marmalade. \n \n \n What do you say? \n \n 1. 'I'll have a few slices of gouda please! I love cheese so so much' \n 2. 'No thank you! I love to look at cheeese, but I am unfortunatly burdened with a cheese allergy and can not eat any \n 3. Make your excuses and head back to the town square" + note(3))
        if (choice === "1"){
            choice = prompt("Marmalade takes a few of your coins, and hands you your slices. you eat them immediately and remark on the loveliness of their aroma and flavor. \n \n \n What do you do next? \n \n 1. Return to the town square" + note(1))
            if (choice === "1"){
                atTownSquare()
            } else { errorMessage }
        }else if(choice === "2"){
            choice = prompt("Marmalade hands you a slice of dairy-free imitation gouda. \n 'I keep this in stock just for rats like you! I think everyone deserves a slice of cheese, you'll love it, I promise!' \n \n \n What do you do next? \n \n 1. Thank Marmalade and return to the town square" + note(1))
            if (choice === "1"){
                atTownSquare()
            } else { errorMessage }
        }else if(choice === "3"){
            atTownSquare()
        } else { errorMessage() }
    }
}

function atFeatherMerchant(){
    if(hasBeenToGhostTown == true){
        if (hasSeenGhostFeatherMerchant === false){
            hasSeenGhostFeatherMerchant = true
            let choice = prompt("You walk to the stall but the merchant is gone, so are the feathers. Except for one that's fallen onto the floor - it's small and somewhat pearlescent. It reminds you of a ghost. \n \n \n What do you do? \n \n 1. Pick up the feather \n 2. Go back to the town square" + note(2))
            if (choice === "1" ){
                choice = prompt("You reach for the feather but it dissolves into what is barely even a pile of dust. \n \n \n What do you do? \n \n 1. Return to the town square" + note(1))
                if (choice === "1"){
                    atTownSquare()
                } else { errorMessage() }
            }
            else if (choice === "2"){
                atTownSquare()
            } else { errorMessage() }
        } else {
            let choice = prompt("You arrive at the feathre merchant's stall. Neither merchant nor feather await you - it is empty. \n \n \n What do you do next? \n \n 1. Return to town square" + note(1))
            if (choice === "1"){
                atTownSquare()
            } else { errorMessage() }
        }
    } else {
        if (hasTalkedWithFeatherMerchant === false){
            hasTalkedWithFeatherMerchant = true
            let choice = prompt("You arrive at the feather merchant's stall. It is somewhat small, but filled with every type of feather imaginable. One specific feather catches your eye - it is gold, with flecks of ruby red. \n 'Oh, I see that feather has caught your eye', the feather merchant says. 'Unfortunatly I can't let you have that one, but I can give you this one' \n You look at the feather - it's the same color as your fur, and you could wear it on your head. \n \n \n How do you procede? \n \n 1. Take the feather and return to the town square \n 2. Leave the feather and return to the town square")
            if (choice === "1"){
                hasFeather = true
                atTownSquare()
            } else if (choice === "2"){
                atTownSquare()
            } else { errorMessage() }
        } else {
            let message = "You walk back to the feather merchant's stall. The same feathers are on the table, but the merchant is busy with another customer."
            if (hasFeather == false){
                message+= " You wish you had taken the feather that was offered to you earlier but you missed your chance."
            }
            message+= "\n \n \n What do you do next? \n \n 1. Return to the town square "
            let choice = prompt(message + note(1))
            if (choice === "1"){
                atTownSquare()
            } else ( errorMessage() )
        }
    }
}

function headToCastle(){
    let choice = prompt("You walk for a bit towards the castle. There is a moat you can hop over, and a suspicious looking rock \n \n \n What do you want to do? \n \n 1. Keep walking to the castle \n 2. Look at the rock " + note(2))

    //user keeps going to the castle
    if (choice === "1"){  
        headToCastle2()
    //user looks at the rock
    } else if (choice === "2"){
        choice = prompt ("You pickup the rock and notice it is not a rock at all, but a pretend rock! it says 'key' on it. You think about how this must be a fake rock to store keys in. \n \n \n What do you want to do? \n \n 1. Get the key out of the rock \n 2. Put the rock back \n \n " + note(2))

        //user gets key out of rock 
        if(choice === "1"){
            let message = "You find a latch and pry open a secret key compartment. "
            if (hasKey === false){
                hasKey = true
                message += "There is a key! The key is beautiful and old and adorned with lovely markings and makes you feel nice and happy. It looks to be made of gold and rubys. "
            } else {
                message += "But you already got the key earlier so the secret compartment is empty. "
                if (hasUsedKey === true){
                    message += "You even used it to unlock the castle. "
                }
            }
            message += "\n \n \n What do you want to do next? \n 1. Continue to the castle \n 2. Go back to town"
            choice = prompt(message + note(2))

            // continue to castle
            if(choice === "1"){
                headToCastle2()
            // go back to towns
            } else if (choice == 2){
                atTownSquare()
            } else { errorMessage() }

        //user puts rock down
        } else if (choice == 2){
            choice = prompt("You place the rock back down without looking at it any further. \n \n \n What do you want to do next? \n \n 1. Continue to the castle \n 2. Go back to town")
            // continue to castle
            if(choice === "1"){
                headToCastle2()
            // go back to towns
            } else if (choice == 2){
                atTownSquare()
            } else { errorMessage() }

        }else { errorMessage() }
        



    } else { errorMessage() }
    

}

function tryToOpenDoor(){
    if(hasKey === false){
        choice = prompt("You try the door but it is locked. \n \n \n What are you gonna do next? \n \n 1. Head back to town" + note(1))
        if (choice === "1"){
            atTownSquare()
        } else { errorMessage() }
    } else if (hasKey === true) {
        message = ""
        if (hasUsedKey === false){
            hasUsedKey = true;
            message = "The door is locked. But its cheery demeanor reminds you something you felt before... Oh! You remember you have the key you found earlier. Taking it out of your pouch you realize it matches the doorknob's own decorative style. \n You place it into the keyhole and turn the key. It clicks open. \n \n \n What are you going to do now that you've unlocked the door \n \n 1. Go inside the castle \n 2. Go back to town"
        } else {
            message = "The door is just as unlocked as it was after you unlocked it earlier, so you can still go in. \n \n \n What next for you? \n \n 1. Go inside the castle \n 2. Go back to town"
        }
        choice = prompt(message + note(2))
        // go to castle
        if (choice === "1"){
            atCastleHall()
        // go to town
        } else if (choice ===2 ){
            atTownSquare()
        } else {errorMessage() }
    }
}

function headToCastle2(){
    let message = ""
    if (hasBeenToCastleMoat == false){
        message += "There is no water in the moat, and It looks like there is no bridge either, but you have your strong rat legs so you jump across and continue up the path. \n You arrive at the castle after walking for what seems like anything beteween 2 mintues or two hours. The castle gate is up and there is no guard to guide your, nor is there a guide to guard you. You walk through the lifted gates untill you reach a set of large cheerfully ominous oak doors. \n \n \n What course of action are you compelled to take? "
        hasBeenToCastleMoat = true;
    } else {
        message+= "You jump the moat like you did last time, then you walk, walk, walk and walk some more. You arrive at the castle. The gates are still up so you go the door. \n \n What are you going to do?"
    }
    message+= "\n \n 1. Knock on the door \n 2. Try to open the door"
    let choice = prompt(message + note(2))

    //user knocks on the door
    if (choice === "1"){
        choice = prompt("You think you hear a rustling behind the door, but when you knock, no one opens it for you. \n \n \n What do you do next? \n \n 1. Try to open the door \n 2. Return to town" + note(2))
        if (choice === "1"){tryToOpenDoor()} 
        else if (choice === "2" ){ atTownSquare() }
        else { errorMessage() }

    //user tries to open the door
    } else if (choice === "2"){
        tryToOpenDoor()
    } else { errorMessage() }
}

function atFarms(){
    let choice = prompt("You arrive at one of the farms. It is verdant and green and full of little fruits growing from bushes and from trees and growing straight out of the grass and even out of the ground. You see a lovely hammock nearby. \n \n \n What do you want to do? \n \n 1. Take a nap in the hammock \n 2. Go back to town" + note(2))
    if (choice === "1"){
        choice = prompt("You decide to take a lovely nap. You manage to swing yourself up into the hammock and you get nice and comfortable. Before you know it you are falling asleep. \n After what seems like a long time, you wake up. You feel so refreshed! But when you look at the sky, you notice the sun is in the exact same place, even though the clouds are different. Weird. \n \n \n What do you want to do? \n \n 1. Head back to the farms \n 2. Head back to town" + note(2))
        if (choice === "1"){
            atFarms()
        } else if (choice === "2"){
            atTownSquare()
        } else { errorMessage() }
    } else if (choice === "2"){
        atTownSquare()
    } else { errorMessage() }
}


function atCastleHall(){
    if (hasBeenToCastle === false){
        hasBeenToCastle = true
        let choice = prompt("You push the doors open. They are very heavy and old and creeky and the hinges haven't been oiled in a while. They open into the great hall. \n There are detailed tapestries depicting courtly life are hanging from the walls. It seem's almost like there is a feast happening, tables are lines up with entrees and drinks and appetizers and sweets adorning their centers. The food is still hot, but there is no one here. the throne at the head of the room is empty \n \n \n What do you do next? \n \n 1. Return to Town" + note(1))
        if (choice === "1"){ atTownSquare() }
        else { errorMessage() }
    } else {
        if (hasComeBackToCastle === false){
            hasComeBackToCastle = true
            let choice = prompt("You go back into the castle hall. \nThe feast is still setup, but you notice that the food has cooled down by now. \nYou go to inspect the tapestries and notice that while they are depicting castle life with scenes of grand feasts, thrilling hunts, and epic battles, the scenes are empty. Like sets without any actors, displaying only where things should take place. Last time you where here, there where hunter's in the tapestry forests, and knights in the tapestry battle fields, but now there is no one. \n You walk towards the regal Bobouse's throne, only to notice that the king mouse's royal robes and crown are in a pile - as if someone like someone had been wearing them before dissapearing into thin air. \n \n \n How are you going to continue? \n \n 1. Return to town" + note(1))
            if (choice === "1") { atTownSquare() }
            else { errorMessage() }
        } else {
            let choice = prompt("You return to the hall. The food has begun to rot, and an unpleasant scent fills the room. You feel like there must be someone there, but no one is. You think you can almost hear a distant scuttling. \n \n \n What do you do? \n \n 1. Walk to the throne" + note(1))
            if (choice === "1"){
                alert("You walk towards the throne, and take a seat. You put on the royal robes and place the crown on your head.")
            } else { errorMessage() }
        }   
    }
}

// startGame()

