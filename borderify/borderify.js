document.body.style.border = "25px dashed purple";
function getPage() {
    browser.tabs.query({ currentWindow: true, active: true })
        .then((tabs) => {
            console.log(tabs[0].url);
        })
}
getPage();