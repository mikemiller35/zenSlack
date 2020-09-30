# zenSlack

A Slackbot coming soon...

## What you need to do 

- Have a slack webhook setup
- Have a Zendesk trigger configured, and a Zendesk http target

Deploy this with serverless
`serverless deploy --slackhook "whatever your slack webhook is"`

Get the api endpoint, and put that into your Zendesk http target.  

Currently this is written to handle the following payload from Zendesk (In the Zendesk trigger)

```
{"source": "Zendesk","ticket_requester": "{{ticket.requester.name}}","requester_email": "{{ticket.requester.email}}","ticket_url": "{{ticket.url}}"}
```