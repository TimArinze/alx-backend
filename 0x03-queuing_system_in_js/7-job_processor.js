const kue = require('kue')

const blacklisted = ['4153518780', '4153518781'];

const queue = kue.createQueue({
    currency: 2 //for process two jobs at a time
})

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100)
    if (blacklisted.includes(phoneNumber)) {
        return job.on('failed', (job, err) => {
            message = `Phone number ${phoneNumber} is blacklisted`
        })
    } else {
        if (job.progress(50, 100)) {
            console.log(`Sending Notification to ${phoneNumber}, with message: ${message}`)
        }
    }
    done()
}

queue.process('push_notification_code_2', (job, done) => {
    const {phoneNumber, message } = job.data
    sendNotification(phoneNumber, message, job, done)
})
