/* Fetch JSON and add chart to element. */
async function display(controlsId) {
    const controls = document.querySelector(controlsId);
    const controlsData = new FormData(controls);
    const queryString = new URLSearchParams(controlsData).toString();
    const url = `http://127.0.0.1:5000/data?${queryString}`;

    const response = await fetch(url);
    const data = await response.json();
    const chartId = `#${data['_chart']}`;
    const display = document.querySelector(chartId);
    new chartXkcd.XY(display, data);
}

/* Refresh all charts. */
async function displayAll() {
    const allControls = document.querySelectorAll(".controls");
    for (let i = 0; i < allControls.length; i++) {
	const controls = allControls[i];
	const controlsId = `#${controls.id}`;
	await display(controlsId);
    }
}
