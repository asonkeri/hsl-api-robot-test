*** Settings ***
Library     Collections
Library     ./lib/HslApiLibrary.py    ${SUT URL}


*** Variables ***
${SUT URL}      https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql


*** Test Cases ***
Should Return Correct Stop Name By Id
    ${response}=    Query    stop(id: "HSL:2323253") {name}
    Should Be Equal    ${response.data.stop.name}    Meteorinsilta

Should Return Error On Incorrect Query Argument
    ${response}=    Query    stop(foo: "bar") {name}    expected_status=500
    Should Be Equal    ${response.errors[0].errorType}    ValidationError
