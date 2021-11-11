/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
var dayOfTheWeek = function(day, month, year) {
    const a=new Date()
    a.setYear(year)
    a.setMonth(month-1)
    a.setDate(day)
    const day1  = a.toDateString().split(' ')[0]
    console.log(a)
    const map = {
        'Sat':'Saturday',
        'Mon':'Monday',
        'Wed':'Wednesday',
        'Thu':'Thursday',
        'Tue':'Tuesday',
        'Fri':'Friday',
        'Sun':'Sunday'
    };
    console.log(day1)
    return map[day1]
};