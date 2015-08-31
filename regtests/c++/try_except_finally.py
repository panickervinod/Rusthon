'''
c++ finally
'''

def myfunc():
	## TODO - update __open__ so it throws an error
	#f = open('/tmp/nosuchfile')

	a = False
	try:
		raise RuntimeError('oops')
	except RuntimeError:
		print 'caught RuntimeError OK'
		a = True

	assert a == True

	b = False

	try:
		print('trying something that will fail...')
		print('some call that fails at runtime')
		f = open('/tmp/nosuchfile')
	except RuntimeError:
		print 'this should not happen'
	except IOError:
		print 'CAUGHT IOError OK'
		raise RuntimeError('rethrowing error')
	except:
		print('CAUGHT UNKNOWN EXECEPTION')
		## raise another exception
		raise RuntimeError('got unknown exception')
	finally:
		print('FINALLY')
		b = True

	assert b == True

def main():
	myfunc()
