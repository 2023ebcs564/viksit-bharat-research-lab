const counters=document.querySelectorAll(".counter");

counters.forEach(counter=>{

    counter.innerText="0";

    const updateCounter=()=>{

        const target=+counter.dataset.target;

        const count=+counter.innerText;

        const increment=Math.ceil(target/100);

        if(count<target){

            counter.innerText=count+increment;

            setTimeout(updateCounter,20);

        }

        else{

            counter.innerText=target;

        }

    };

    updateCounter();

});

const images=document.querySelectorAll(".gallery-image");

const lightbox=document.getElementById("lightboxImage");

const modal=new bootstrap.Modal(document.getElementById("lightboxModal"));

images.forEach(image=>{

    image.addEventListener("click",()=>{

        lightbox.src=image.src;

        modal.show();

    });

});

const backToTopButton=document.getElementById("backToTop");

if(backToTopButton){

    backToTopButton.addEventListener("click",()=>{

        window.scrollTo({

            top:0,

            behavior:"smooth",

        });

    });

}