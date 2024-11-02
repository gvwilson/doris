/* Fetch JSON and add chart to #display element. */
async function display() {
    const form = document.querySelector("#selections");
    const formData = new FormData(form);
    const queryString = new URLSearchParams(formData).toString();
    const url = `http://127.0.0.1:5000/data?${queryString}`;

    const response = await fetch(url);
    const data = await response.json();
    const display = document.querySelector('#chart');
    new chartXkcd.XY(display, data);
}
