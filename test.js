window.alert = function () {
    return false;
}

var submitButton = document.getElementById("electableLessonList_filter_submit")
var electButton = document.getElementById('306610')

/* while (true) {
    var submitButton = document.getElementById("electableLessonList_filter_submit")
    setTimeout('submitButton.click()', 1000)
    // submitButton.click()

    var electButton = document.getElementById('306610')
    setTimeout("electButton.click()", 1000)
    // electButton.click()
} */

// for (i = 0; i < 5; i++) {

//     setTimeout('submitButton.click()', 1000)
//     // submitButton.click()

//     setTimeout("electButton.click()", 1000)
//     // electButton.click()
//     console.log('attempt', i)
// }

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function Tutor() {
    for (let i = 1; i < 20; i++) {
        submitButton.click()
        await sleep(3000);
        electButton.click()
        console.log('attempt', i);
    }
}
Tutor()