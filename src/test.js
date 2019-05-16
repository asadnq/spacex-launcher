const arr = ['pro', 'gram', 'merit'];

const match = inpt => {
  let check;
  arr.map(i => {
    for (let iol = 0; iol < inpt.length; iol++) {
      if (check == i) {
        console.log(i);
        check = '';
      }
      check += inpt[iol];
    }
  });
};
match('pro');