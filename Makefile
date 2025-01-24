run:
	docker run -d --name my_container --rm -e TELEGRAM_BOT_TOKEN="7111576325:AAEQ6wXGmlnfg6GZzfooLiBN5PWv7S1V9tg" image-test:v_1
stop:
	docker stop my_container