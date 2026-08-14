# Let's create an index.html file with self-contained CSS/SVG and a professional interactive editor
# so that when uploaded to GitHub and hosted via GitHub Pages, it works instantly out of the box.

github_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>80th Independence Day Teacher Certificate - CM SOE GIRLS SAHIBGANJ</title>
<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background: #1e1e24;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 20px 10px;
}

/* ================= TOP CONTROL BAR ================= */
.editor-panel {
    background: #ffffff;
    padding: 16px 20px;
    border-radius: 12px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
    align-items: center;
    width: min(1000px, 98%);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}

.editor-panel input {
    flex: 1 1 220px;
    padding: 10px 14px;
    border: 1.5px solid #ccc;
    border-radius: 8px;
    font-size: 15px;
    outline: none;
    transition: 0.2s border-color;
}

.editor-panel input:focus {
    border-color: #123b72;
}

.btn {
    padding: 11px 22px;
    border: none;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: transform 0.1s, opacity 0.2s;
}

.btn:active {
    transform: scale(0.98);
}

.btn-update {
    background: #123b72;
    color: white;
}

.btn-download {
    background: #138808;
    color: white;
}

/* ================= CERTIFICATE WRAPPER ================= */
.cert-wrapper {
    position: relative;
    width: min(1000px, 96vw);
    aspect-ratio: 1.414 / 1; /* A4 Ratio */
    background: #ffffff;
    border: 8px solid #d4af37;
    box-shadow: 0 12px 40px rgba(0,0,0,0.6);
    overflow: hidden;
}

/* Outer & Inner Border lines */
.cert-border-inner {
    position: absolute;
    inset: 6px;
    border: 3px solid #123b72;
    pointer-events: none;
    z-index: 5;
}

.corner-accent {
    position: absolute;
    width: 32px;
    height: 32px;
    border: 3px solid #d4af37;
    z-index: 6;
}
.c-tl { top: 12px; left: 12px; border-right: none; border-bottom: none; }
.c-tr { top: 12px; right: 12px; border-left: none; border-bottom: none; }
.c-bl { bottom: 12px; left: 12px; border-right: none; border-top: none; }
.c-br { bottom: 12px; right: 12px; border-left: none; border-top: none; }

/* Tricolor Wavy Watermark Background */
.tiranga-bg {
    position: absolute;
    inset: 0;
    opacity: 0.14;
    z-index: 2;
    pointer-events: none;
    display: flex;
    flex-direction: column;
}

.band {
    flex: 1;
    width: 100%;
}

.band-saffron { background: #FF6800; }
.band-white { background: #FFFFFF; }
.band-green { background: #138808; }

/* Main Card Content */
.cert-content {
    position: absolute;
    inset: 22px;
    z-index: 10;
    text-align: center;
    background: rgba(255, 255, 255, 0.88);
    border: 1.5px solid rgba(181, 142, 35, 0.5);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 2.2% 4%;
}

/* Header Typography */
.school-title {
    font-size: clamp(16px, 2.7vw, 30px);
    font-weight: 900;
    color: #e87717;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-shadow: 1px 1px 0px #fff;
}

.school-subtitle {
    font-size: clamp(10px, 1.2vw, 15px);
    font-weight: 700;
    color: #123b72;
    letter-spacing: 1px;
}

/* Ashoka Chakra */
.chakra-box {
    margin: 2px auto;
}

/* Certificate Title */
.title-main {
    font-size: clamp(20px, 3.4vw, 40px);
    font-weight: 900;
    letter-spacing: 4px;
    color: #09245d;
    line-height: 1.1;
}

.title-sub {
    font-size: clamp(11px, 1.4vw, 17px);
    letter-spacing: 5px;
    font-weight: 700;
    color: #333;
}

.gold-divider {
    width: 45%;
    height: 2px;
    margin: 4px auto;
    background: linear-gradient(to right, transparent, #123b72, transparent);
}

.tag-presented {
    display: inline-block;
    align-self: center;
    margin: 2px auto;
    padding: 4px 22px;
    background: #0b2d65;
    color: #fff;
    font-size: clamp(9px, 1.1vw, 13px);
    font-weight: 700;
    letter-spacing: 2px;
    border-radius: 3px;
}

/* Teacher Name */
.teacher-display-name {
    font-family: 'Brush Script MT', 'Segoe Script', cursive, serif;
    font-size: clamp(24px, 4.2vw, 52px);
    font-style: italic;
    color: #081b4c;
    font-weight: 700;
    margin: 2px 0;
    text-shadow: 1px 1px 0 #fff;
}

.name-underline {
    width: 50%;
    height: 1.5px;
    background: #102653;
    margin: 0 auto 4px;
}

.message-text {
    width: 82%;
    margin: 0 auto;
    font-size: clamp(10px, 1.2vw, 15px);
    line-height: 1.4;
    color: #2b2b2b;
}

/* Occasion */
.happy-tag {
    font-size: clamp(10px, 1.3vw, 15px);
    color: #e27600;
    font-weight: 800;
    letter-spacing: 2px;
}

.occasion-title {
    font-size: clamp(14px, 2.1vw, 25px);
    color: #08742d;
    font-weight: 900;
    letter-spacing: 1px;
}

.date-tag {
    font-size: clamp(9px, 1.1vw, 13px);
    font-weight: 700;
    color: #17305f;
    letter-spacing: 2px;
}

/* Bottom Footer (Badge & Signature) */
.footer-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 4px;
}

.badge-seal {
    width: clamp(52px, 7vw, 75px);
    height: clamp(52px, 7vw, 75px);
    border-radius: 50%;
    background: #10254f;
    border: 3.5px solid #e1bd4d;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: clamp(6px, 0.8vw, 9px);
    font-weight: 800;
    line-height: 1.2;
    box-shadow: 0 3px 8px rgba(0,0,0,0.25);
}

.signature-box {
    width: clamp(130px, 20vw, 200px);
    text-align: center;
}

.signature-name-text {
    font-family: 'Brush Script MT', 'Segoe Script', cursive, serif;
    font-size: clamp(14px, 1.8vw, 22px);
    font-style: italic;
    font-weight: 700;
    color: #081b4c;
}

.sig-line {
    height: 1.5px;
    background: #102653;
    margin: 2px 0;
}

.sig-label {
    font-size: clamp(7px, 0.85vw, 11px);
    font-weight: 700;
    letter-spacing: 2px;
    color: #333;
}

/* ================= PRINT STYLES ================= */
@media print {
    body {
        background: transparent;
        padding: 0;
    }
    .editor-panel {
        display: none !important;
    }
    .cert-wrapper {
        width: 100vw;
        height: 100vh;
        border-width: 6px;
        box-shadow: none;
    }
    @page {
        size: A4 landscape;
        margin: 0;
    }
}
</style>
</head>
<body>

<!-- TOP INPUT EDITOR -->
<div class="editor-panel">
    <input type="text" id="inputName" value="Teacher Name" placeholder="Teacher Name">
    <input type="text" id="inputMsg" value="In recognition of your dedication, valuable contribution and selfless service to the school and students." placeholder="Appreciation Message">
    <input type="text" id="inputSign" value="Rishabh Kr. Sharma" placeholder="Signature Name">
    <button class="btn btn-update" onclick="updateCert()">Preview</button>
    <button class="btn btn-download" onclick="window.print()">Print / Save PDF</button>
</div>

<!-- CERTIFICATE -->
<div class="cert-wrapper">
    <!-- Inner Borders & Accents -->
    <div class="cert-border-inner"></div>
    <div class="corner-accent c-tl"></div>
    <div class="corner-accent c-tr"></div>
    <div class="corner-accent c-bl"></div>
    <div class="corner-accent c-br"></div>

    <!-- Flag Background Watermark -->
    <div class="tiranga-bg">
        <div class="band band-saffron"></div>
        <div class="band band-white"></div>
        <div class="band band-green"></div>
    </div>

    <!-- Certificate Content -->
    <div class="cert-content">
        <div>
            <div class="school-title">CM SOE GIRL'S SAHIBGANJ</div>
            <div class="school-subtitle">CM SCHOOL OF EXCELLENCE (GIRLS), SAHIBGANJ</div>
        </div>

        <!-- Ashoka Chakra SVG -->
        <div class="chakra-box">
            <svg viewBox="0 0 100 100" width="38" height="38">
                <circle cx="50" cy="50" r="46" fill="none" stroke="#173f91" stroke-width="6"/>
                <circle cx="50" cy="50" r="8" fill="#173f91"/>
                <g stroke="#173f91" stroke-width="2.5">
                    <line x1="50" y1="50" x2="50" y2="4" />
                    <line x1="50" y1="50" x2="61.9" y2="6.5" />
                    <line x1="50" y1="50" x2="73" y2="13.7" />
                    <line x1="50" y1="50" x2="82.5" y2="24.4" />
                    <line x1="50" y1="50" x2="89.8" y2="37.5" />
                    <line x1="50" y1="50" x2="94" y2="50" />
                    <line x1="50" y1="50" x2="89.8" y2="62.5" />
                    <line x1="50" y1="50" x2="82.5" y2="75.6" />
                    <line x1="50" y1="50" x2="73" y2="86.3" />
                    <line x1="50" y1="50" x2="61.9" y2="93.5" />
                    <line x1="50" y1="50" x2="50" y2="96" />
                    <line x1="50" y1="50" x2="38.1" y2="93.5" />
                    <line x1="50" y1="50" x2="27" y2="86.3" />
                    <line x1="50" y1="50" x2="17.5" y2="75.6" />
                    <line x1="50" y1="50" x2="10.2" y2="62.5" />
                    <line x1="50" y1="50" x2="6" y2="50" />
                    <line x1="50" y1="50" x2="10.2" y2="37.5" />
                    <line x1="50" y1="50" x2="17.5" y2="24.4" />
                    <line x1="50" y1="50" x2="27" y2="13.7" />
                    <line x1="50" y1="50" x2="38.1" y2="6.5" />
                    <line x1="50" y1="50" x2="56.2" y2="5.4" />
                    <line x1="50" y1="50" x2="67.5" y2="9.8" />
                    <line x1="50" y1="50" x2="32.5" y2="9.8" />
                    <line x1="50" y1="50" x2="43.8" y2="5.4" />
                </g>
            </svg>
        </div>

        <div>
            <div class="title-main">CERTIFICATE</div>
            <div class="title-sub">OF APPRECIATION</div>
            <div class="gold-divider"></div>
        </div>

        <div>
            <div class="tag-presented">PROUDLY PRESENTED TO</div>
            <div class="teacher-display-name" id="displayTeacher">Teacher Name</div>
            <div class="name-underline"></div>
            <div class="message-text" id="displayMsg">
                In recognition of your dedication, valuable contribution and selfless service to the school and students.
            </div>
        </div>

        <div>
            <div class="happy-tag">HAPPY</div>
            <div class="occasion-title">80TH INDEPENDENCE DAY</div>
            <div class="date-tag">★ &nbsp; 15 AUGUST 2026 &nbsp; ★</div>
        </div>

        <div class="footer-row">
            <div class="badge-seal">
                <span>★</span>
                <span>JAI HIND</span>
                <span>VANDE</span>
                <span>MATARAM</span>
                <span>★</span>
            </div>

            <div class="signature-box">
                <div class="signature-name-text" id="displaySign">Rishabh Kr. Sharma</div>
                <div class="sig-line"></div>
                <div class="sig-label">SIGNATURE / PRINCIPAL</div>
            </div>
        </div>
    </div>
</div>

<script>
function updateCert() {
    const name = document.getElementById('inputName').value.trim() || 'Teacher Name';
    const msg = document.getElementById('inputMsg').value.trim() || 'In recognition of your dedication, valuable contribution and selfless service to the school and students.';
    const sign = document.getElementById('inputSign').value.trim() || 'Rishabh Kr. Sharma';

    document.getElementById('displayTeacher').textContent = name;
    document.getElementById('displayMsg').textContent = msg;
    document.getElementById('displaySign').textContent = sign;
}
</script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(github_index_html)

readme_content = """# 80th Independence Day Teacher Certificate 🇮🇳

CM School of Excellence (Girls), Sahibganj ke Independence Day (15 August 2026) Certificate Generator.

## Features
- Fully responsive & print-ready layout (A4 Landscape).
- Live name, message, aur signature editor.
- High-resolution SVG Ashoka Chakra aur Tiranga background.
- Direct **Save as PDF** / **Print** option.

## Live Demo
GitHub Pages enable karke direct live website chala sakte hain!
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("index.html and README.md ready for GitHub!")