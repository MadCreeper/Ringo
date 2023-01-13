export function zeroPad(num, places) {
    var zero = places - num.toString().length + 1;
    return Array(+(zero > 0 && zero)).join("0") + num;
}

export function formatDateTime(dateToFormat) {
    const d = new Date(dateToFormat)
    const year = d.getFullYear()
    const monthName = d.getMonth()
    const date = d.getDate() 
    const formatted = `${year}年${monthName+1}月${date}日 ${zeroPad(d.getHours(), 2)}:${zeroPad(d.getMinutes(), 2)}` 
    return formatted;
}