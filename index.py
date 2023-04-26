html_front = """
<!DOCTYPE html>
<!-- Coding By CodingNepal - youtube.com/codingnepal -->
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Playable Piano JavaScript | CodingNepal</title>
    <link rel="stylesheet" href="style.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <div class="wrapper">
      <header>
        <h2>Playable PIANO</h2>
        <div class="column volume-slider">
          <span>Volume</span><input type="range" min="0" max="1" value="0.5" step="any">
        </div>
        <div class="column keys-checkbox">
          <span>Show Keys</span><input type="checkbox" checked>
        </div>
      </header>
      <ul class="piano-keys">
        <li class="key white" data-key="a"><span>a</span></li>
        <li class="key black" data-key="w"><span>w</span></li>
        <li class="key white" data-key="s"><span>s</span></li>
        <li class="key black" data-key="e"><span>e</span></li>
        <li class="key white" data-key="d"><span>d</span></li>
        <li class="key white" data-key="f"><span>f</span></li>
        <li class="key black" data-key="t"><span>t</span></li>
        <li class="key white" data-key="g"><span>g</span></li>
        <li class="key black" data-key="y"><span>y</span></li>
        <li class="key white" data-key="h"><span>h</span></li>
        <li class="key black" data-key="u"><span>u</span></li>
        <li class="key white" data-key="j"><span>j</span></li>
        <li class="key white" data-key="k"><span>k</span></li>
        <li class="key black" data-key="o"><span>o</span></li>
        <li class="key white" data-key="l"><span>l</span></li>
        <li class="key black" data-key="p"><span>p</span></li>
        <li class="key white" data-key=";"><span>;</span></li>
      </ul>
    </div>
  </body>
</html>
"""

html_front = """
<!DOCTYPE html>
<!-- Coding By CodingNepal - youtube.com/codingnepal -->
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Playable Piano JavaScript | CodingNepal</title>
    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #E3F2FD;
}
.wrapper {
  padding: 35px 40px;
  border-radius: 20px;
  background: #141414;
}
.wrapper header {
  display: flex;
  color: #B2B2B2;
  align-items: center;
  justify-content: space-between;
}
header h2 {
  font-size: 1.6rem;
}
header .column {
  display: flex;
  align-items: center;
}
header span {
  font-weight: 500;
  margin-right: 15px;
  font-size: 1.19rem;
}
header input {
  outline: none;
  border-radius: 30px;
}
.volume-slider input {
  accent-color: #fff;
}
.keys-checkbox input {
  height: 30px;
  width: 60px;
  cursor: pointer;
  appearance: none;
  position: relative;
  background: #4B4B4B
}
.keys-checkbox input::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 5px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #8c8c8c;
  transform: translateY(-50%);
  transition: all 0.3s ease;
}
.keys-checkbox input:checked::before {
  left: 35px;
  background: #fff;
}
.piano-keys {
  display: flex !important;
  list-style: none !important;
  margin-top: 40px !important;
}
.piano-keys .key {
  cursor: pointer;
  user-select: none;
  position: relative;
  text-transform: uppercase;
}
.piano-keys .black {
  z-index: 2;
  width: 44px;
  height: 140px;
  margin: 0 -22px 0 -22px;
  border-radius: 0 0 5px 5px;
  background: linear-gradient(#333, #000);
}
.piano-keys .black.active {
  box-shadow: inset -5px -10px 10px rgba(255,255,255,0.1);
  background:linear-gradient(to bottom, #000, #434343);
}
.piano-keys .white {
  height: 230px;
  width: 70px;
  border-radius: 8px;
  border: 1px solid #000;
  background: linear-gradient(#fff 96%, #eee 4%);
}
.piano-keys .white.active {
  box-shadow: inset -5px 5px 20px rgba(0,0,0,0.2);
  background:linear-gradient(to bottom, #fff 0%, #eee 100%);
}
.piano-keys .key span {
  position: absolute;
  bottom: 20px;
  width: 100%;
  color: #A2A2A2;
  font-size: 1.13rem;
  text-align: center;
}
.piano-keys .key.hide span {
  display: none;
}
.piano-keys .black span {
  bottom: 13px;
  color: #888888;
}

@media screen and (max-width: 815px) {
  .wrapper {
    padding: 25px;
  }
  header {
    flex-direction: column;
  }
  header :where(h2, .column) {
    margin-bottom: 13px;
  }
  .volume-slider input {
    max-width: 100px;
  }
  .piano-keys {
    margin-top: 20px;
  }
  .piano-keys .key:where(:nth-child(9), :nth-child(10)) {
    display: none;
  }
  .piano-keys .black {
    height: 100px;
    width: 40px;
    margin: 0 -20px 0 -20px;
  }
  .piano-keys .white {
    height: 180px;
    width: 60px;
  }
}

@media screen and (max-width: 615px) {
  .piano-keys .key:nth-child(13),
  .piano-keys .key:nth-child(14),
  .piano-keys .key:nth-child(15),
  .piano-keys .key:nth-child(16),
  .piano-keys .key :nth-child(17) {
    display: none;
  }
  .piano-keys .white {
    width: 50px;
  }
}
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <div class="wrapper">
      <header>
        <h2>Playable PIANO</h2>
        <div class="column volume-slider">
          <span>Volume</span><input type="range" min="0" max="1" value="0.5" step="any">
        </div>
        <div class="column keys-checkbox">
          <span>Show Keys</span><input type="checkbox" checked>
        </div>
      </header>
      <ul class="piano-keys">
        <li class="key white" data-key="a"><span>a</span></li>
        <li class="key black" data-key="w"><span>w</span></li>
        <li class="key white" data-key="s"><span>s</span></li>
        <li class="key black" data-key="e"><span>e</span></li>
        <li class="key white" data-key="d"><span>d</span></li>
        <li class="key white" data-key="f"><span>f</span></li>
        <li class="key black" data-key="t"><span>t</span></li>
        <li class="key white" data-key="g"><span>g</span></li>
        <li class="key black" data-key="y"><span>y</span></li>
        <li class="key white" data-key="h"><span>h</span></li>
        <li class="key black" data-key="u"><span>u</span></li>
        <li class="key white" data-key="j"><span>j</span></li>
        <li class="key white" data-key="k"><span>k</span></li>
        <li class="key black" data-key="o"><span>o</span></li>
        <li class="key white" data-key="l"><span>l</span></li>
        <li class="key black" data-key="p"><span>p</span></li>
        <li class="key white" data-key=";"><span>;</span></li>
      </ul>
    </div>
        <script>

const pianoKeys = document.querySelectorAll(".piano-keys .key"),
volumeSlider = document.querySelector(".volume-slider input"),
keysCheckbox = document.querySelector(".keys-checkbox input");

let allKeys = [],
audio = new Audio(`a.wav`); // by default, audio src is "a" tune

const playTune = (key) => {
    audio.src = `${key}.wav`; // passing audio src based on key pressed 
    audio.src = 'melody_roland.wav';
    audio.play(); // playing audio

    const clickedKey = document.querySelector(`[data-key="${key}"]`); // getting clicked key element
    clickedKey.classList.add("active"); // adding active class to the clicked key element
    setTimeout(() => { // removing active class after 150 ms from the clicked key element
        clickedKey.classList.remove("active");
    }, 150);
}

pianoKeys.forEach(key => {
    allKeys.push(key.dataset.key); // adding data-key value to the allKeys array
    // calling playTune function with passing data-key value as an argument
    key.addEventListener("click", () => playTune(key.dataset.key));
});

const handleVolume = (e) => {
    audio.volume = e.target.value; // passing the range slider value as an audio volume
}

const showHideKeys = () => {
    // toggling hide class from each key on the checkbox click
    pianoKeys.forEach(key => key.classList.toggle("hide"));
}

const pressedKey = (e) => {
    // if the pressed key is in the allKeys array, only call the playTune function
    if(allKeys.includes(e.key)) playTune(e.key);
}

keysCheckbox.addEventListener("click", showHideKeys);
volumeSlider.addEventListener("input", handleVolume);
document.addEventListener("keydown", pressedKey);
        </script>

  </body>
</html>
"""

# html_front = """
# <!DOCTYPE html>
# <html lang="en">
#
# <head>
#     <title>My page</title>
#     <meta charset="utf-8" />
#     <meta name="viewport" content="minimum-scale=1, initial-scale=1, width=device-width" />
#     <script src="https://unpkg.com/react@latest/umd/react.development.js" crossorigin="anonymous"></script>
#     <script src="https://unpkg.com/react-dom@latest/umd/react-dom.development.js"></script>
#     <script src="https://unpkg.com/@material-ui/core@latest/umd/material-ui.development.js"
#         crossorigin="anonymous"></script>
#     <script src="https://unpkg.com/babel-standalone@latest/babel.min.js" crossorigin="anonymous"></script>
#     <!-- Fonts to support Material Design -->
#     <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
#     <!-- Icons to support Material Design -->
#     <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
#     <link rel="stylesheet" href="style.css" type="text/css">
# </head>
#
# <body>
#     <div id="root"></div>
#     <script type="text/babel">
#         const {
#             Button,
#             CssBaseline,
#             makeStyles,
#             Paper,
#             Table,
#             TableBody,
#             TableCell,
#             TableContainer,
#             TableHead,
#             TableRow,
#             withStyles
#         } = MaterialUI;
#
#
#         const StyledTableCell = withStyles((theme) => ({
#             head: {
#                 backgroundColor: theme.palette.common.black,
#                 color: theme.palette.common.white,
#             },
#             body: {
#                 fontSize: 14,
#             },
#         }))(TableCell);
#
#         const StyledTableRow = withStyles((theme) => ({
#             root: {
#                 '&:nth-of-type(odd)': {
#                     backgroundColor: theme.palette.action.hover,
#                 },
#             },
#         }))(TableRow);
#
#         function createData(name, calories, fat, carbs, protein) {
#             return { name, calories, fat, carbs, protein };
#         }
#
#         const rows = [
#             createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
#             createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
#             createData('Eclair', 262, 16.0, 24, 6.0),
#             createData('Cupcake', 305, 3.7, 67, 4.3),
#             createData('Gingerbread', 356, 16.0, 49, 3.9),
#         ];
#
#         const useStyles = makeStyles({
#             table: {
#                 minWidth: 700,
#             },
#         });
#
#         const CustomTable = () => {
#             const classes = useStyles();
#
#             return (
#                 <TableContainer component={Paper}>
#                     <Table className={classes.table} aria-label="customized table">
#                         <TableHead>
#                             <TableRow>
#                                 <StyledTableCell>Dessert (100g serving)</StyledTableCell>
#                                 <StyledTableCell align="right">Calories</StyledTableCell>
#                                 <StyledTableCell align="right">Fat&nbsp;(g)</StyledTableCell>
#                                 <StyledTableCell align="right">Carbs&nbsp;(g)</StyledTableCell>
#                                 <StyledTableCell align="right">Protein&nbsp;(g)</StyledTableCell>
#                             </TableRow>
#                         </TableHead>
#                         <TableBody>
#                             {rows.map((row) => (
#                                 <StyledTableRow key={row.name}>
#                                     <StyledTableCell component="th" scope="row">
#                                         {row.name}
#                                     </StyledTableCell>
#                                     <StyledTableCell align="right">{row.calories}</StyledTableCell>
#                                     <StyledTableCell align="right">{row.fat}</StyledTableCell>
#                                     <StyledTableCell align="right">{row.carbs}</StyledTableCell>
#                                     <StyledTableCell align="right">{row.protein}</StyledTableCell>
#                                 </StyledTableRow>
#                             ))}
#                         </TableBody>
#                     </Table>
#                 </TableContainer>
#             );
#         }
#
#         const App = () => {
#             return (
#                 <CustomTable />
#             );
#         }
#
#         ReactDOM.render(
#             <div>
#                 <CssBaseline />
#                 <App />
#             </div>,
#             document.querySelector('#root'),
#         );
#     </script>
# </body>
#
# </html>
# """