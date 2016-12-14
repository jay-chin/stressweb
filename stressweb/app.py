import subprocess
import itertools

from flask import Flask, request
app = Flask(__name__)

stress_bin = '/usr/bin/stress'
defaults = {
        '--cpu' : '1',
        '--timeout' : '10s',
        '--vm' : '1',
        '--io' : '1',
        '--vm-bytes' : '128M',
}

dict2list = lambda d: list(itertools.chain.from_iterable(d.items()))

@app.route("/")
def hello():
    return " ".join(dict2list(defaults)) 

@app.route("/run")
def run():
    cmd = [stress_bin]

    defaults['--cpu'] = request.args.get('cpu', defaults['--cpu'])
    defaults['--timeout'] = request.args.get('timeout', defaults['--timeout'])
    defaults['--io'] = request.args.get('io', defaults['--io'])
    defaults['--vm'] = request.args.get('vm', defaults['--vm'])
    defaults['--vm-bytes'] = request.args.get('vm-bytes', defaults['--vm-bytes'])

    cmd.extend(dict2list(defaults))

    app.logger.info("Running cmd : %s" % ' '.join(cmd))
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
    out,err = p.communicate()
    app.logger.info("Output: %s" % out)
    return out 

if __name__ == "__main__":
    app.run()
