const amazonlogo = document.querySelector(".logo");
amazonlogo.addEventListener("click",()=>{
    window.location.href = "https://www.amazon.in/";
});

const all = document.querySelector(".All");
all.addEventListener("change",()=>{
    let output = all.value;
    console.log(output);
    console.log('output')
    if (output === "Alexa Skills"){
        window.location.href = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dalexa-skills&field-keywords=&crid=12JXFFSDX1C5Y&sprefix=%2Calexa-skills%2C1014";
    }else if(output == 'Amazon Devices'){
        window.location.href = "https://www.amazon.in/s?i=amazon-devices&crid=3T429NKI397KB&sprefix=%2Camazon-devices%2C379&ref=nb_sb_noss";
    }else if(output === 'Amazon Fashion'){
        window.location.href = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dfashion&field-keywords=&crid=3RSGNOAWZQXFX&sprefix=%2Cfashion%2C1160";
    }else if(output === 'Furnitures'){
        window.location.href = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Dfurniture&field-keywords=&crid=2Q41D5Q5RO9NM&sprefix=%2Cfurniture%2C281&discounts-widget=%2522%257B%255C%2522state%255C%2522%253A%257B%255C%2522refinementFilters%255C%2522%253A%257B%257D%257D%252C%255C%2522version%255C%2522%253A1%257D%2522";
    }else if(output === 'Mobiles'){
        window.location.href = 'https://www.amazon.in/b?node=976419031';
    }else if(output === 'Beauty'){
        window.location.href = 'https://www.amazon.in/b?node=1355016031';
    }else if(output === 'Books'){
        window.location.href = 'https://www.amazon.in/b?node=976389031&discounts-widget=%2522%257B%255C%2522state%255C%2522%253A%257B%255C%2522refinementFilters%255C%2522%253A%257B%257D%257D%252C%255C%2522version%255C%2522%253A1%257D%2522';
    }else if(output === 'Electronics'){
        window.location.href = 'https://www.amazon.in/b?node=976419031';
    }else if(output === "Baby"){
        window.location.href = "https://www.amazon.in/s?k=Baby&i=baby&crid=3IQQ11VPM0V0J&sprefix=%2Cbaby%2C2321&ref=nb_sb_noss"
    }
});


const area = document.querySelector(".location");
const landmark=document.querySelector(".area");
area.addEventListener("click",()=>{
    landmark.style.display="block";
});
const code=document.querySelector(".loc");
code.addEventListener("click",()=>{
    landmark.style.display="none";
}
)
function change()
{
    const pincode=document.querySelector(".postcode").value
    area.innerHTML=`Delivering to India ${pincode}<br/><b>Update Location`
    landmark.style.display = 'none';
}


 //login/signin
const loginn = document.querySelector(".login");
loginn.addEventListener("click",()=>{
    window.location.href="location.html";
})


function cartitems(){
    window.location.href='Amazoncart.html';
}