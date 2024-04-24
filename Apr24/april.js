const month = "April";

const dateCheck = (date) => {
  if (date === 24) {
    return true;
  } else {
    return false;
  }
};

module.exports = { month, dateCheck };
