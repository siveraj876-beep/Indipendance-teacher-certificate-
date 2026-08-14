<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>80th Independence Day Teacher Certificate</title>

<style>

*{
    box-sizing:border-box;
}

body{
    margin:0;
    background:#222;
    font-family:Georgia,"Times New Roman",serif;
}


/* ================= EDITOR ================= */

.editor{
    background:white;
    padding:15px;
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    justify-content:center;
}

.editor input{
    width:280px;
    padding:11px;
    border:1px solid #aaa;
    border-radius:8px;
    font-size:16px;
}

.editor button{
    padding:11px 20px;
    border:0;
    border-radius:8px;
    background:#123b72;
    color:white;
    font-size:16px;
    font-weight:bold;
}

.editor .download{
    background:#138808;
}


/* ================= CERTIFICATE ================= */

#certificate{

    position:relative;

    width:min(1200px,96vw);

    aspect-ratio:16/10;

    margin:25px auto;

    overflow:hidden;

    background:white;

    border:10px solid #d7b64a;

    box-shadow:0 0 30px #000;

}


/* ================= SCHOOL PHOTO ================= */

.school-photo{

    position:absolute;

    inset:0;

    width:100%;

    height:100%;

    object-fit:cover;

    object-position:center;

    filter:saturate(.95) contrast(.95);

}


/* Light transparent layer */

.photo-light{

    position:absolute;

    inset:0;

    background:
        rgba(255,255,255,.40);

}


/* ================= WAVING TIRANGA ================= */

.flag{

    position:absolute;

    left:-6%;

    top:-4%;

    width:112%;

    height:108%;

    opacity:.24;

    z-index:3;

    pointer-events:none;

}


.band{

    position:absolute;

    left:0;

    width:100%;

    height:33.3333%;

    animation:
        wave 5s ease-in-out infinite;

}


/* SAFFRON */

.saffron{

    top:0;

    background:#FF6800;

    clip-path:polygon(

        0 10%,
        8% 2%,
        16% 14%,
        25% 4%,
        34% 16%,
        44% 3%,
        54% 15%,
        64% 4%,
        74% 17%,
        84% 3%,
        94% 15%,
        100% 7%,

        100% 100%,
        0 100%

    );

}


/* WHITE */

.white{

    top:33.3333%;

    background:#FFFFFF;

    clip-path:polygon(

        0 7%,
        10% 19%,
        20% 5%,
        30% 18%,
        40% 4%,
        50% 19%,
        60% 5%,
        70% 18%,
        80% 4%,
        90% 20%,
        100% 7%,

        100% 100%,
        0 100%

    );

}


/* GREEN */

.green{

    top:66.6666%;

    background:#138808;

    clip-path:polygon(

        0 11%,
        9% 3%,
        18% 18%,
        28% 5%,
        38% 20%,
        48% 4%,
        58% 18%,
        68% 5%,
        78% 20%,
        88% 4%,
        96% 17%,
        100% 8%,

        100% 100%,
        0 100%

    );

}


/* WAVE ANIMATION */

@keyframes wave{

    0%,100%{

        transform:
        translateX(-1.5%)
        skewY(-.7deg);

    }

    50%{

        transform:
        translateX(1.5%)
        skewY(.7deg);

    }

}


/* ================= CONTENT ================= */

.content{

    position:absolute;

    z-index:10;

    left:8%;

    right:8%;

    top:7%;

    bottom:7%;

    text-align:center;

    padding:3.5% 5%;

    background:
        rgba(255,255,255,.70);

    border:
        2px solid
        rgba(181,142,35,.8);

    box-shadow:
        0 0 20px rgba(0,0,0,.12);

}


/* SCHOOL NAME */

.school-name{

    font-family:Arial,sans-serif;

    font-weight:900;

    font-size:
        clamp(22px,3.1vw,46px);

    color:#e87717;

    text-shadow:
        1px 1px #fff,
        2px 2px #775000;

    letter-spacing:1px;

}


.school-sub{

    font-family:Arial,sans-serif;

    font-weight:bold;

    font-size:
        clamp(12px,1.35vw,20px);

    color:#123b72;

    margin-top:4px;

}


/* ================= CHAKRA ================= */

.chakra{

    width:62px;

    height:62px;

    margin:8px auto 4px;

    border:
        4px solid #173f91;

    border-radius:50%;

    background:
        repeating-conic-gradient(
            #173f91 0 4deg,
            transparent 4deg 15deg
        );

    position:relative;

}


.chakra:after{

    content:"";

    position:absolute;

    width:12px;

    height:12px;

    border-radius:50%;

    background:#173f91;

    left:50%;

    top:50%;

    transform:
        translate(-50%,-50%);

}


/* ================= TITLE ================= */

.cert-title{

    font-size:
        clamp(28px,5vw,70px);

    font-weight:900;

    letter-spacing:3px;

    color:#09245d;

    text-shadow:
        2px 2px #fff;

}


.appreciation{

    font-size:
        clamp(15px,2vw,27px);

    letter-spacing:6px;

    font-weight:bold;

}


.rule{

    width:45%;

    height:2px;

    margin:8px auto;

    background:#17305f;

}


/* ================= PRESENTED ================= */

.presented{

    display:inline-block;

    margin-top:8px;

    padding:8px 34px;

    background:#0b2d65;

    color:white;

    font-family:Arial,sans-serif;

    font-size:
        clamp(11px,1.4vw,20px);

    font-weight:bold;

    letter-spacing:2px;

}


/* ================= TEACHER NAME ================= */

#teacherName{

    margin:10px auto 4px;

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size:
        clamp(32px,5.3vw,76px);

    font-style:italic;

    color:#081b4c;

    text-shadow:
        2px 2px #fff;

}


.name-line{

    width:55%;

    height:2px;

    background:#102653;

    margin:auto;

}


/* ================= MESSAGE ================= */

.message{

    margin:9px auto 0;

    width:78%;

    font-size:
        clamp(11px,1.35vw,19px);

    line-height:1.4;

}


/* ================= INDEPENDENCE DAY ================= */

.happy{

    margin-top:9px;

    font-size:
        clamp(17px,2.2vw,30px);

    color:#e27600;

    font-weight:bold;

    letter-spacing:3px;

}


.independence{

    font-family:Arial,sans-serif;

    font-size:
        clamp(20px,3vw,42px);

    color:#08742d;

    font-weight:900;

}


.date{

    font-size:
        clamp(14px,1.7vw,24px);

    font-weight:bold;

    letter-spacing:3px;

    margin-top:3px;

}


/* ================= BADGE ================= */

.badge{

    position:absolute;

    left:5%;

    bottom:5%;

    z-index:20;

    width:88px;

    height:88px;

    border-radius:50%;

    background:#10254f;

    border:
        6px solid #e1bd4d;

    color:white;

    display:grid;

    place-items:center;

    text-align:center;

    font-family:Arial,sans-serif;

    font-size:10px;

    font-weight:bold;

    line-height:1.15;

}


/* ================= SIGNATURE ================= */

.signature{

    position:absolute;

    right:7%;

    bottom:5%;

    width:24%;

    z-index:20;

    text-align:center;

}


.signature-name{

    font-family:
        "Brush Script MT",
        "Segoe Script",
        cursive;

    font-size:
        clamp(15px,2vw,28px);

    font-style:italic;

    white-space:nowrap;

}


.signature-line{

    height:2px;

    background:#102653;

}


.signature-label{

    font-family:Arial,sans-serif;

    font-size:
        clamp(8px,1vw,13px);

    font-weight:bold;

    letter-spacing:3px;

}


/* ================= MOBILE ================= */

@media(max-width:650px){

    .editor{

        flex-direction:column;

    }

    .editor input,
    .editor button{

        width:100%;

    }

    #certificate{

        margin:14px auto;

        border-width:5px;

    }

    .content{

        left:4%;

        right:4%;

        top:5%;

        bottom:5%;

        padding:3%;

    }

    .badge{

        width:55px;

        height:55px;

        border-width:4px;

        font-size:6px;

    }

}


/* ================= PRINT ================= */

@media print{

    body{

        background:white;

    }

    .editor{

        display:none;

    }

    #certificate{

        width:100vw;

        margin:0;

        border-width:6px;

        box-shadow:none;

        -webkit-print-color-adjust:exact;

        print-color-adjust:exact;

    }

    @page{

        size:landscape;

        margin:0;

    }

}

</style>

</head>


<body>


<!-- ================= EDITOR ================= -->

<div class="editor">

    <input
        id="nameInput"
        value="Teacher Name"
        placeholder="Teacher Name"
    >

    <input
        id="msgInput"
        value="In recognition of your dedication, valuable contribution and service to the school and students."
        placeholder="Certificate Message"
    >

    <button onclick="updateCertificate()">

        Preview Certificate

    </button>


    <button
        class="download"
        onclick="window.print()"
    >

        Download / Save PDF

    </button>

</div>



<!-- ================= CERTIFICATE ================= -->

<div id="certificate">


    <!--
        IMPORTANT:
        Apni uploaded photo ko
        assets/school-photo.jpg
        naam se rakho.
    -->

    <img
        class="school-photo"
        src="assets/school-photo.jpg"
        alt="CM SOE GIRLS SAHIBGANJ"
    >


    <div class="photo-light"></div>


    <!-- WAVING TRANSPARENT TRICOLOUR -->

    <div class="flag">

        <div class="band saffron"></div>

        <div class="band white"></div>

        <div class="band green"></div>

    </div>



    <!-- ================= CERTIFICATE CONTENT ================= -->

    <div class="content">


        <div class="school-name">

            CM SOE GIRL'S SAHIBGANJ

        </div>


        <div class="school-sub">

            CM SOE GIRLS SAHIBGANJ

        </div>


        <!-- ASHOKA CHAKRA -->

        <div class="chakra"></div>


        <div class="cert-title">

            CERTIFICATE

        </div>


        <div class="appreciation">

            OF APPRECIATION

        </div>


        <div class="rule"></div>


        <div class="presented">

            PROUDLY PRESENTED TO

        </div>


        <div id="teacherName">

            Teacher Name

        </div>


        <div class="name-line"></div>


        <div
            id="message"
            class="message"
        >

            In recognition of your dedication,
            valuable contribution and service
            to the school and students.

        </div>


        <div class="happy">

            HAPPY

        </div>


        <div class="independence">

            80TH INDEPENDENCE DAY

        </div>


        <div class="date">

            ★ &nbsp; 15 AUGUST 2026 &nbsp; ★

        </div>


    </div>



    <!-- ================= BADGE ================= -->

    <div class="badge">

        ★<br>

        JAI HIND<br>

        VANDE<br>

        MATARAM<br>

        ★

    </div>



    <!-- ================= SIGNATURE ================= -->

    <div class="signature">

        <div class="signature-name">

            Rishabh Kr. Sharma

        </div>


        <div class="signature-line"></div>


        <div class="signature-label">

            SIGNATURE

        </div>

    </div>


</div>



<script>

/* ================= UPDATE CERTIFICATE ================= */

function updateCertificate(){

    let name =
        document
        .getElementById("nameInput")
        .value
        .trim();


    let message =
        document
        .getElementById("msgInput")
        .value
        .trim();


    if(name === ""){

        name = "Teacher Name";

    }


    if(message === ""){

        message =
        "In recognition of your dedication, valuable contribution and service to the school and students.";

    }


    document
    .getElementById("teacherName")
    .textContent = name;


    document
    .getElementById("message")
    .textContent = message;

}

</script>


</body>

</html>
