const userRoleEnum = Object.freeze({
    NONE: 0,
    ADMIN: 1,
});
const convertIntoToUserRole = function (i) {
    for (var p in userRoleEnum) {
        if (p === i || userRoleEnum[p] === i) {
            return p;
        }
    }
    return userRoleEnum.NONE
}
export { userRoleEnum, convertIntoToUserRole }