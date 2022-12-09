export function formatDateTime(dateTime) {
    let newDate = dateTime.replace("T", " ");
    newDate = newDate.replace("Z", "");
    return newDate;
}