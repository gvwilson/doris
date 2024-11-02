async function display() {
    const response = await fetch('http://127.0.0.1:5000/data');
    const data = await response.json();
    console.log(data);
}
