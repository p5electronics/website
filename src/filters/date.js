const { DateTime } = require("luxon");

module.exports = (dateObj, format = 'LLLL dd, yyyy') => {
    let date;
    if (dateObj instanceof Date) {
        date = DateTime.fromJSDate(dateObj, {
            zone: 'America/New_York', 
            locale: "en"
        });
    } else {
        date = DateTime.fromISO(dateObj, {
            zone: 'America/New_York', 
            locale: "en"
        });
    }
    if (!date.isValid) {
        console.error(`Invalid DateTime: ${dateObj}`);
        return dateObj; 
    }
    return date.toFormat(format);
};
