const btn1 = document.getElementById('inc');

elementClicked= false;

btn1.addEventListener('click', function handleClick()){
    if (elementClicked){
        return;
    }
    elementClicked= true
}
