window.alert = function () {
    return false;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function main() {
    for (let i = 1; i < 10; i++) {
        var submitButton = document.getElementById("electableLessonList_filter_submit")
        submitButton.click()
        await sleep(1000);
        var electButton = document.getElementById('306610')
        electButton.click()
        await sleep(1000);
        console.log('attempt', i);

    }
}
main()