export function formatDateTime(dateToFormat) {
    const d = new Date(dateToFormat)
    const year = d.getFullYear()
    const monthName = d.getMonth()
    const date = d.getDate() 
    const formatted = `${year}年${monthName+1}月${date}日 ${d.getHours()}:${d.getMinutes()}` 
    return formatted;
}