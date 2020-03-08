
---
title: "The Learning Line Follower"
author: James O'Toole
date: 2020-03-01T17:51:39Z
draft: true
---
Be warned, this tale is a tragedy.

For Christmas, my father bought me an Arduino robot kit with 4 wheels some eyes and ears. It came with light  (and sonar) sensors. I decided to conduct supervised learning with a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain) model. Two front light sensor point vertically down, reading the grounds ability to reflect infrared light. The kit came with black tape to lay on the floor. I aimed to teach the robot to follow the line, programming it to remember 1KB: a weighted guess at a set of movements given the last two things it saw (input reads). The code I wrote is in this [code repository](https://github.com/SmileyJames/arduino_markov).

I built the robot following the Ikea like instructions, easy stuff (think electronic lego and a little mechano). After a period of writing the program's first draft and some debugging, I let the dumb buggy loose in the kitchen, starting with It's eyeballs to the black tape circuit. I switch it on and click on my remote to start - It trashed violently with a preference to always drive backwards, I rewarded it with 'up arrow' remote control clicks if it ever went forward and punished with 'down arrow' clicks when it went backwards or turned the wrong way. It seemed like behavior initially went well and then suddenly only went forwards - speeding towards the door frame.

I was ecstatic with the outcome (crashes aside) - it had had a go and even got a little better for a bit, however clearly the program needed a little bit of work. A few iterations and I discovered a number of issues relating to integer overflow, especially in the . Some trial and error in the kitchen helped me tweak some (run-time static) variables.

This yielded reasonable results. After half an hour of training the robot went forward and attempted the corner a majority of times. I thought a simple hand programmed - a non-learning approach could probably beat it.

One faces problems when working on a device with a small memory footprint. Once It learns that 1 choice is 100% likely, given a scenario of input, it will make the choice again and then either be punished or rewarded - here it is hard to decide how the program to operate. One option is to stop making changes. My solution attempts some "easing", allowing 100 - 0 choices change - there is an argument that this is sub optimal.

With regular training and saving the model to persistent storage, the robot started to make good progress. I was pleased with the results and continuing to make small improvements to the code.

Then the battery died, and wouldn't recharge.
