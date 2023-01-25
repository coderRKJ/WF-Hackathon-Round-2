console.log("JS Loaded");
var counter = 1;

const inputRange = document.getElementById("rateRange");
const inputRangeLabel = inputRange.labels[0];
const defaultHTML = inputRangeLabel.innerHTML;
inputRangeLabel.innerHTML = defaultHTML + inputRange.value;
inputRange.addEventListener("input", () => {
    inputRangeLabel.innerHTML = defaultHTML + inputRange.value;
});

async function startRequests(ele) {
    inputRange.setAttribute('disabled', '');
    ele.setAttribute('class', "btn btn-lg btn-danger");
    ele.innerHTML = "Stop";
    ele.setAttribute('onclick', 'stopRequests(this);');

    const url = new URL('http://localhost:3001/process');
    url.searchParams.append('id', `${counter}`);
    url.searchParams.append('value', counter * 2);
    console.log(url.href);
    await fetch(url)
        .then((res) => res.json())
        .then((data) => console.log(data))
        .catch((error) => console.error(error));

    const metricsurl  = new URL(window.location.href);
    console.log(metricsurl.href);
    metricsurl.pathname = 'metrics';
    console.log(metricsurl.href);
    await fetch(metricsurl)
        .then((res) => res.json())
        .then((data) => console.log(data))
        .catch((error) => console.error(error));
}

async function stopRequests(ele) {
    inputRange.removeAttribute('disabled');
    ele.setAttribute('class', "btn btn-lg btn-primary");
    ele.innerHTML = "Start";
    ele.setAttribute('onclick', 'startRequests(this);');
}

async function activeToggle(ele, port) {
    console.log(`Checked:${ele.checked}, Port:${port}`);
}

async function errorToggle(ele, port) {
    console.log(`Checked:${ele.checked}, Port:${port}`);
}