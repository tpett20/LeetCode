// 2383. Minimum Hours of Training to Win a Competition
/*
You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.
You are also given two 0-indexed integer arrays energy and experience, both of length n.
You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.
Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].
Before starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.
Return the minimum number of training hours required to defeat all n opponents.
*/

var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
    let trainingHrs = 0
    let numOpponents = energy.length
    for (let i = 0; i < numOpponents; i++) {
        if (initialEnergy <= energy[i] || initialExperience <= experience[i]) {
            let energyDiff = (energy[i] + 1) - initialEnergy
            if (energyDiff > 0) {
                initialEnergy += energyDiff
                trainingHrs += energyDiff
            }
            let expDiff = (experience[i] + 1) - initialExperience
            if (expDiff > 0) {
                initialExperience += expDiff
                trainingHrs += expDiff
            }
        }
        initialEnergy -= energy[i]
        initialExperience += experience[i]
    }
    return trainingHrs
};

const initialEnergy = 5
const initialExperience = 3
const energy = [1,4,3,2]
const experience = [2,6,3,1]

console.log(minNumberOfHours(initialEnergy, initialExperience, energy, experience))