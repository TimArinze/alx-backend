import kue from 'kue'


const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
	phoneNumber: '08137339240',
	message: 'You won a lottery',
}).save((error) => {
	if (error) {
		console.log('Notification job failed')
	} else {
		console.log(`Notification job created: ${job.id}`)
	}
})

job.on('complete', () => {
	console.log(`Notification job completed`)
})

job.on('failed', () => {
	console.log(`Notification job failed`)
})
