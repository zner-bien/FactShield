const canvas = document.getElementById("particles-canvas");

if (canvas) {

    const ctx = canvas.getContext("2d");

    let particles = [];

    let mouse = {
        x: null,
        y: null
    };

    function resize() {

        canvas.width = window.innerWidth;

        canvas.height = window.innerHeight;

    }

    resize();

    window.addEventListener("resize", resize);

    window.addEventListener("mousemove", function(e){

        mouse.x = e.clientX;

        mouse.y = e.clientY;

    });

    class Particle{

        constructor(){

            this.x = Math.random()*canvas.width;

            this.y = Math.random()*canvas.height;

            this.radius = Math.random()*2+1;

            this.speedX = (Math.random()-.5)*0.3;

            this.speedY = (Math.random()-.5)*0.3;

        }

        update(){

            this.x += this.speedX;

            this.y += this.speedY;

            if(this.x<0) this.x=canvas.width;

            if(this.x>canvas.width) this.x=0;

            if(this.y<0) this.y=canvas.height;

            if(this.y>canvas.height) this.y=0;

            if(mouse.x){

                const dx=this.x-mouse.x;

                const dy=this.y-mouse.y;

                const distance=Math.sqrt(dx*dx+dy*dy);

                if(distance<120){

                    this.x += dx*0.015;

                    this.y += dy*0.015;

                }

            }

        }

        draw(){

            ctx.beginPath();

            ctx.fillStyle="rgba(255,255,255,.45)";

            ctx.arc(this.x,this.y,this.radius,0,Math.PI*2);

            ctx.fill();

        }

    }

    for(let i=0;i<120;i++){

        particles.push(new Particle());

    }

    function animate(){

        ctx.clearRect(0,0,canvas.width,canvas.height);

        particles.forEach(p=>{

            p.update();

            p.draw();

        });

        requestAnimationFrame(animate);

    }

    animate();

}