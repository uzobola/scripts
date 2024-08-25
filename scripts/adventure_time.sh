#!/bin/bash
 
# Objective: Create your own text-based "Create Your Own Adventure story" using Bash scripting. 
# Apply knowledge of loops and conditionals to make the story interactive, 
# Allow the player to make choices that affect the outcome.
 

 
# Function to display text with a typing effect 
# P.S: I chose 'type_text' over 'read -p' and "print_text" just because it makes it type cooler! (Thanks to ChatGPT!)
type_text() {
    text="$1"
    for ((i=0; i<${#text}; i++)); do
        echo -n "${text:$i:1}"
        sleep 0.03
    done
    echo
}
 
# Function to get player choice
get_choice() {
    read -p "Enter your choice (1 or 2): " choice
    echo $choice
}
 
# The Story begins...
type_text "Welcome to 'A Date Gone Wrong' - Your choice, Your Story!"
echo " "
type_text " After so many left swipes, you've got a date!"
echo " "
type_text " You've been looking forward to this date for weeks...But, as you arrive at the restaurant..."
echo " "
echo " "
 
 
 
# First choice
type_text "1. You realize you forgot your wallet (Oh shucks!)"
type_text "2. You notice your date texting someone else (What in the blazes!?! ... but hey, let's play it cool)"
echo " "
echo " "
 
 
# Collect the choice in a variable
choice=$(get_choice)
 
if [ "$choice" == "1" ]; then
    type_text "So, You've forgotten your wallet. What do you do?"
    echo " "
    type_text "1. Be honest and explain the situation to your date (At least you won't have to wash dishes at the end of the dinner to cover your portion.) "
    type_text "2. Pretend everything is fine and hope your date will pay (Bad idea but hey, that's on you!) "
    echo " "
    echo " "
        choice=$(get_choice)
 
    if [ "$choice" == "1" ]; then
        type_text "Your honesty is appreciated. Your date offers to split the bill using venmo. (Whew, crisis averted!) "
        type_text "The evening continues pleasantly, and you both laugh about the incident.( Hnmm, they might be a keeper!)"
        echo " "
        type_text "Congratulations! Despite the hiccup, your date was a success!"
        type_text "(P.S: You are lucky you did not end up washing dishes to cover your portion of the bill!)"
    else
        type_text "You try to act normal, but when the bill arrives, your date notices your discomfort."
        type_text "They're upset by your dishonesty, and the date ends awkwardly.(Well ... like we did not see that coming. )"
        echo " "
        type_text "Game Over, greedy bugger! You probably should have come clean before you wolfed down the meal!"
    fi
else   
    type_text "You see your date texting someone else. How do you react?"
    echo " "
    type_text "1. Confront them about it ( Why do you have to be so extra? For crying out loud it's just the first date!)"
    type_text "2. Ignore it and try to engage them in conversation (You might as well enjoy the evening right?)"
    echo " "
    echo " "
        choice=$(get_choice)
       
    if [ "$choice" == "1" ]; then
        type_text "You respectfully ask about the texting. Your date apologizes, explaining it was a work emergency.(Being Understanding is one of your strongest traits)"
        type_text "They put their phone away, and you have a great conversation for the rest of the evening."
        echo " "
        type_text " See, there was no need to be extra! Congratulations, your communication skills saved the date!"
    else
        type_text "You try to ignore the texting, but your date remains distracted throughout dinner. (Well, this is awkward...)"
        type_text "The evening drags on uncomfortably, and you both leave feeling disappointed.(Bummer! Such a sad waste of a nice outfit and good perfume.) "
        echo " "
        type_text "Game Over!"
        type_text " Well, I guess it pays to address issues directly. On the bright side, at least you dodged a bullet!"
    fi
fi
 
echo " "
type_text "Thanks for playing 'A Date Gone Wrong'!"
echo " "
echo " "
type_text "Hope this ridiculous adventure  made you smile, cackle or Guffaw( Yup! it's a real word, please look it up)"
echo " " 
