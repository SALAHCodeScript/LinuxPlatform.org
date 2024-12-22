<style>
body {
    background: rgb(5 5 10);
}
body .boxes {
    display: flex;
    justify-content: space-between;
}
body .boxes .box {
    padding: 5px;
    background: rgb(100 0 0);
    font-size: 50px;
    border: 5px solid;
    border-radius: 10px;
}
.bash {
    display: flex;
    flex-direction: column;
}
.markdown {
    font-family: '0xProto Nerd Font Mono';
}
.markdown1 {
    font-size: 50px;
}
.markdown2 {
    font-size: 40px;
}
.prompt1 {
    color: rgb(255 125 25);
}
.prompt2 {
    color: grey;
}
.prompt3 {
    color: rgb(255 255 0);
}
.prompt4 {
    color: rgb(0 100 255);
}

.arrow {
    color: rgb(100 255 0);
}
.command {
    color: grey;
}
</style>

<div class="boxes">
    <div class="box box1">BOX 1</div>
    <div class="box box2">BOX 2</div>
    <div class="box box3">BOX 3</div>
</div>

<div class='bash'>
    <p><span class='markdown markdown1 prompt1'> </span><span class='markdown markdown1 prompt2'> </span><span class='markdown markdown1 prompt3'> </span><span class='markdown markdown1 prompt4'>Marksdown</p>
    <p><span class='markdown markdown2 arrow'>❯ </span><span class='markdown markdown2 command'>$HOME</span></p>
</div>
