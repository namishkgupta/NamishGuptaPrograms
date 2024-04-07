function calculatePosition() {
    const origin = document.getElementById('origin').value;    
    const finalOrigin = format(origin)
    const distOrigin = format2(origin)

    const destination = document.getElementById('destination').value;    
    const finalDestination = format(destination)
    const distDestination = format2(destination)

    const mapUrl = "https://www.google.com/maps/embed/v1/directions?key=AIzaSyBs5sPfD3BjUJQdTXo9vlyYZ5_LCb3ImyQ&&origin="+finalOrigin+"&destination="+finalDestination+"&avoid=tolls|highways";

    const mapIframe = document.getElementById('map-iframe');

    mapIframe.setAttribute('src', mapUrl);

}

function format(stringd){
    const splitString = stringd.split(" ");
    const joinedString = splitString.join("+");
    return joinedString;

}

function format2(stringd){
    const splitString = stringd.split(" ");
    const joinedString = splitString.join("%20");
    return joinedString;

}
