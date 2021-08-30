// function myFuction() {
//     alert("login succesfully !!!!")
// }

function logOut() {
    alert("Logout Successfully !!!")
}
// function addpostbtn() {
//     alert("Add Post Successfully !!!")
// }
// function updatepost() {
//     alert("Update Post Successfully !!!")
// }
// function signUp() {
//     alert("Registration Sunccessfully !!!")
// }

var i = 0;
function read() {
    if (!i) {
        document.getElementById("more").style.display = "inline";
        document.getElementById("dots").style.display = "none";
        document.getElementById("readbtn").innerHTML = "Read less";
        i = 1;
    } else {
        document.getElementById("more").style.display = "none";
        document.getElementById("dots").style.display = "inline";
        document.getElementById("readbtn").innerHTML = "Read more";
        i = 0;
    }
}