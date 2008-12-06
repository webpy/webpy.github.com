---
layout: default
title: Change log
---

# Change log

<dl>

<dt>2008-12-06: 0.3</dt>
<dd>new: replace print with return (<i>backward-incompatible</i>)</dd>
<dd>new: application framework (<i>backward-incompatible</i>)</dd>
<dd>new: modular database system (<i>backward-incompatible</i>)</dd>
<dd>new: templetor reimplementation</dd>
<dd>new: better unicode support</dd>
<dd>new: debug mode (web.config.debug)</dd>
<dd>new: better db pooling</dd>
<dd>new: sessions</dd>
<dd>new: support for GAE</dd>
<dd>new: etag support</dd>
<dd>new: web.openid module</dd>
<dd>new: web.nthstr</dd>
<dd>fix: various form.py fixes</dd>
<dd>fix: python 2.6 compatibility</dd>
<dd>fix: file uploads are not loaded into memory</dd>
<dd>fix: SQLLiteral issue (Bug#180027)</dd>
<dd>change: web.background is moved to experimental (<i>backward-incompatible</i>)</dd> 
<dd>improved document generation (tx Colin Rothwell)</dd>
<dt>2008-01-19: 0.23</dt>
<dd>fix: for web.background gotcha (<a href="http://bugs.launchpad.net/webpy/+bug/133079">133079</a>)</dd>
<dd>fix: for postgres unicode bug (<a href="http://bugs.launchpad.net/webpy/+bug/177265">177265</a>)</dd>
<dd>fix: web.profile behavior in python 2.5 (<a href="http://bugs.launchpad.net/webpy/+bug/133080">133080</a>)</dd>
<dd>fix: only uppercase HTTP methods are allowed. (<a href="http://bugs.launchpad.net/webpy/+bug/176415">176415</a>)</dd><dd>fix: transaction error in with statement (<a href="http://bugs.launchpad.net/webpy/+bug/125118">125118</a>)</dd><dd>fix: fix in web.reparam (<a href="http://bugs.launchpad.net/webpy/+bug/162085">162085</a>)</dd><dd>fix: various unicode issues (<a href="http://bugs.launchpad.net/webpy/+bug/137042">137042</a>, <a href="http://bugs.launchpad.net/webpy/+bug/180510">180510</a>, <a href="http://bugs.launchpad.net/webpy/+bug/180549">180549</a>, <a href="http://bugs.launchpad.net/webpy/+bug/180653">180653</a>)</dd>
<dd>new: support for https</dd>
<dd>new: support for secure cookies</dd>
<dd>new: sendmail</dd>
<dd>new: htmlunquote</dd>
</dl>

<dl>
<dt>2007-08-23: 0.22</dt>
<dd>compatibility with new DBUtils API (<a href="https://bugs.launchpad.net/webpy/+bug/122112">122112</a>)</dd>
<dd>fix reloading (<a href="https://bugs.launchpad.net/webpy/+bug/118683">118683</a>)</dd>
<dd>fix compatibility between `changequery` and `redirect` (<a href="https://bugs.launchpad.net/webpy/+bug/118234">118234</a>)</dd>
<dd>fix relative URI in `web.redirect` (<a href="https://bugs.launchpad.net/webpy/+bug/118236">118236</a>)</dd>
<dd>fix `ctx._write` support in built-in HTTP server (<a href="https://bugs.launchpad.net/webpy/+bug/121908">121908</a>)</dd>
<dd>fix `numify` strips things after '.'s (<a href="https://bugs.launchpad.net/webpy/+bug/118644">118644</a>)</dd>
<dd>fix various unicode isssues (<a href="https://bugs.launchpad.net/webpy/+bug/114703">114703</a>, <a href="https://bugs.launchpad.net/webpy/+bug/120644">120644</a>, <a href="https://bugs.launchpad.net/webpy/+bug/124280">124280</a>)</dd>

<dt>2007-05-28: 0.21</dt>
<dd><strong>security fix:</strong> prevent bad characters in headers</dd>
<dd>support for cheetah template reloading                    </dd>
<dd>support for form validation                               </dd>
<dd>new <code>form.File</code>                                           </dd>
<dd>new <code>web.url</code>                                             </dd>
<dd>fix rendering issues with hidden and button inputs        </dd>
<dd>fix 2.3 incompatability with `numify`                     </dd>
<dd>fix multiple headers with same name                       </dd>
<dd>fix web.redirect issues when homepath is not /            </dd>
<dd>new CherryPy wsgi server                                  </dd>
<dd>new nested transactions                                   </dd>
<dd>new sqlliteral                                            </dd>

<dt>2006-05-09: 0.138</dt>
<dd>New function: <code>intget</code></dd>
<dd>New function: <code>datestr</code></dd>
<dd>New function: <code>validaddr</code></dd>
<dd>New function: <code>sqlwhere</code></dd>
<dd>New function: <code>background</code>, <code>backgrounder</code></dd>
<dd>New function: <code>changequery</code></dd>
<dd>New function: <code>flush</code></dd>
<dd>New function: <code>load</code>, <code>unload</code></dd>
<dd>New variable: <code>loadhooks</code>, <code>unloadhooks</code></dd>
<dd>Better docs; generating <a href="documentation">docs</a> from web.py now</dd>
<dd>global variable <code>REAL_SCRIPT_NAME</code> can now be used to work around lighttpd madness</dd>
<dd>fastcgi/scgi servers now can listen on sockets</dd>
<dd><code>output</code> now encodes Unicode</dd>
<dd><code>input</code> now takes optional <code>_method</code> argument</dd>
<dd><strong>Potentially-incompatible change:</strong> <code>input</code> now returns <code>badrequest</code> automatically when <code>requireds</code> aren't found</dd>
<dd><code>storify</code> now takes lists and dictionaries as requests (see docs)</dd>
<dd><code>redirect</code> now blanks any existing output</dd>
<dd>Quote SQL better when <code>db_printing</code> is on</dd>
<dd>Fix delay in <code>nomethod</code></dd>
<dd>Fix <code>urlquote</code> to encode better.</dd>
<dd>Fix 2.3 incompatibility with <code>iters</code> (tx ??)</dd>
<dd>Fix duplicate headers</dd>
<dd>Improve <code>storify</code> docs</dd>
<dd>Fix <code>IterBetter</code> to raise IndexError, not KeyError</dd>
<dt>2006-03-27: 0.137</dt>
<dd>Add function <code>dictfindall</code> (tx Steve Huffman)</dd>
<dd>Add support to <code>autodelegate</code> for arguments</dd>
<dd>Add functions <code>httpdate</code> and <code>parsehttpdate</code></dd>
<dd>Add function <code>modified</code></dd>
<dd>Add support for FastCGI server mode</dd>
<dd>Clarify <code>dictadd</code> documentation (tx Steve Huffman)</dd>
<dd>Changed license to public domain</dd>
<dd>Clean up to use <code>ctx</code> and <code>env</code> instead of <code>context</code> and <code>environ</code></dd>
<dd>Improved support for PUT, DELETE, etc. (tx list)</dd>
<dd>Fix <code>ctx.fullpath</code> (tx Jesir Vargas)</dd>
<dd>Fix sqlite support (tx Dubhead)</dd>
<dd>Fix documentation bug in <code>lstrips</code> (tx Gregory Petrosyan)</dd>
<dd>Fix support for IPs and ports (1/2 tx Jesir Vargas)</dd>
<dd>Fix <code>ctx.fullpath</code> (tx Jesir Vargas)</dd>
<dd>Fix sqlite support (tx Dubhead)</dd>
<dd>Fix documentation bug in <code>lstrips</code> (tx Gregory Petrosyan)</dd>
<dd>Fix <code>iters</code> bug with sets</dd>
<dd>Fix some breakage introduced by Vargas's patch</dd>
<dd>Fix <code>sqlors</code> bug</dd>
<dd>Fix various small style things (tx Jesir Vargas)</dd>
<dd>Fix bug with <code>input</code> ignoring GET input</dd>
<dt>2006-02-22: 0.136 (svn)</dt>
<dd>Major code cleanup (tx to Jesir Vargas for the patch).</dd>
<dt>2006-02-15: 0.135</dt>
<dd>Really fix that mysql regression (tx Sean Leach).</dd>
<dt>2006-02-15: 0.134</dt>
<dd>The <code>StopIteration</code> exception is now caught. This can be used by functions that do things like check to see if a user is logged in. If the user isn't, they can output a message with a login box and raise StopIteration, preventing the caller from executing.</dd>
<dd>Fix some documentation bugs.</dd>
<dd>Fix mysql regression (tx mrstone).</dd>
<dt>2006-02-12: 0.133</dt>
<dd>Docstrings! (tx numerous, esp. Jonathan Mark (for the patch) and Guido van Rossum (for the prod))</dd>
<dd>Add <code>set</code> to web.iters.</dd>
<dd>Make the `len` returned by `query` an int (tx ??).</dd>
<dd><strong>Backwards-incompatible change:</strong> <code>base</code> now called <code>prefixurl</code>.</dd>
<dd><strong>Backwards-incompatible change:</strong> <code>autoassign</code> now takes <code>self</code> and <code>locals()</code> as arguments.</dd>
<dt>2006-02-07: 0.132</dt>
<dd>New variable <code>iters</code> is now a listing of possible list-like types (currently list, tuple, and, if it exists, Set).</dd>
<dd>New function <code>dictreverse</code> turns <code>{1:2}</code> into <code>{2:1}</code>.</dd>
<dd><code>Storage</code> now a dictionary subclass.</dd>
<dd><code>tryall</code> now takes an optional prefix of functions to run.</dd>
<dd><code>sqlors</code> has various improvements.</dd>
<dd>Fix a bunch of DB API bugs.</dd>
<dd>Fix bug with <code>storify</code> when it received multiple inputs (tx Ben Woosley).</dd>
<dd>Fix bug with returning a generator (tx Zbynek Winkler).</dd>
<dd>Fix bug where len returned a long on query results (tx F.S).</dd>


<dt>2006-01-31: 0.131 (not officially released)</dt>
<dd>New function <code>_interpolate</code> used internally for interpolating strings.</dd>
<dd>Redone database API. <code>select</code>, <code>insert</code>, <code>update</code>, and <code>delete</code> all made consistent. Database queries can now do more complicated expressions like <code>$foo.bar</code> and <code>${a+b}</code>. You now have to explicitly pass the dictionary to look up variables in. Pass <code>vars=locals()</code> to get the old functionality of looking up variables .</dd>
<dd>New functions <code>sqllist</code> and <code>sqlors</code> generate certain kinds of SQL.</dd>
<dt>2006-01-30: 0.13</dt>
<dd>New functions <code>found</code>, <code>seeother</code>, and <code>tempredirect</code> now let you do other kinds of redirects. <code>redirect</code> now also takes an optional status parameter. (tx many)</dd>
<dd>New functions <code>expires</code> and <code>lastmodified</code> make it easy to send those headers.</dd>
<dd>New function <code>gone</code> returns a 410 Gone (tx David Terrell).</dd>
<dd>New function <code>urlquote</code> applies url encoding to a string.</dd>
<dd>New function <code>iterbetter</code> wraps an iterator and allows you to do __getitem__s on it.</dd>
<dd>Have <code>query</code> return an <code>iterbetter</code> instead of an iterator.</dd>
<dd>Have <code>debugerror</code> show tracebacks with the innermost frame first.</dd>
<dd>Add <code>__hash__</code> function to <code>threadeddict</code> (and thus, <code>ctx</code>).</dd>
<dd>Add <code>context.host</code> value for the requested host name.</dd>
<dd>Add option <code>db_printing</code> that prints database queries and the time they take.</dd>
<dd>Add support for database pooling (tx Steve Huffman).</dd>
<dd>Add support for passing values to functions called by <code>handle</code>. If you do <code>('foo', 'value')</code> it will add <code>'value'</code> as an argument when it calls <code>foo</code>.</dd>
<dd>Add support for scgi (tx David Terrell for the patch).</dd>
<dd>Add support for web.py functions that are iterators (tx Brendan O'Connor for the patch).</dd>
<dd>Use new database cursors on each call instead of reusing one.</dd>
<dd><code>setcookie</code> now takes an optional <code>domain</code> argument.</dd>
<dd>Fix bug in autoassign.</dd>
<dd>Fix bug where <code>debugerror</code> would break on objects it couldn't display.</dd>
<dd>Fix bug where you couldn't do <code>#include</code>s inline.</dd>
<dd>Fix bug with <code>reloader</code> and database calls.</dd>
<dd>Fix bug with <code>reloader</code> and base templates.</dd>
<dd>Fix bug with CGI mode on certain operating systems.</dd>
<dd>Fix bug where <code>debug</code> would crash if called outside a request.</dd>
<dd>Fix bug with <code>context.ip</code> giving weird values with proxies.</dd>
<dt>2006-01-29: 0.129</dt>
<dd>Add Python 2.2 support.</dd>
<dt>2006-01-28: 0.128</dt>
<dd>Fix typo in <code>web.profile</code>.</dd>
<dt>2006-01-28: 0.127</dt>
<dd>Fix bug in error message if invalid dbn is sent (tx Panos Laganakos).</dd>
<dt>2006-01-27: 0.126</dt>
<dd>Fix typos in Content-Type headers (tx Beat Bolli for the prod).</dd>
<dt>2006-01-22: 0.125</dt>
<dd>Support Cheetah 2.0.</dd>
<dt>2006-01-22: 0.124</dt>
<dd>Fix spacing bug (tx Tommi Raivio for the prod).</dd>
<dt>2006-01-16: 0.123</dt>
<dd>Fix bug with CGI usage (tx Eddie Sowden for the prod).</dd>
<dt>2006-01-14: 0.122</dt>
<dd>Allow DELETEs from <code>web.query</code> (tx Joost Molenaar for the prod).</dd>
<dt>2006-01-08: 0.121</dt>
<dd>Allow import of submodules like <code>pkg.mod.cn</code> (tx Sridhar Ratna).</dd>
<dd>Fix a bug in <code>update</code> (tx Sergey Khenkin).</dd>
<dt>2006-01-05: 0.12</dt>
<dd><strong>Backwards-incompatible change:</strong> <code>db_parameters</code> is now a dictionary.</dd>

<dd><strong>Backwards-incompatible change:</strong> <code>sumdicts</code> is now <code>dictadd</code>.</dd>

<dd>Add support for PyGreSQL, MySQL (tx Hallgrimur H. Gunnarsson).</dd>

<dd>Use HTML for non-Cheetah error message.</dd>

<dd>New function <code>htmlquote()</code>.</dd>

<dd>New function <code>tryall()</code>.</dd>

<dd><code>ctx.output</code> can now be set to a generator. (tx Brendan O'Connor)</dd>

<dt>2006-01-04: 0.117</dt>
<dd>Add support for psycopg 1.x. (tx Gregory Price)</dd>

<dt>2006-01-04: 0.116</dt>
<dd>Add support for Python 2.3. (tx Evan Jones)</dd>

<dt>2006-01-04: 0.115</dt>
<dd>Fix some bugs where database queries weren't reparameterized. Oops!</dd>

<dd>Fix a bug where <code>run()</code> wasn't getting the right functions.</dd>

<dd>Remove a debug statement accidentally left in.</dd>

<dd>Allow <code>storify</code> to be used on dictionaries. (tx Joseph Trent)</dd>

<dt>2006-01-04: 0.114</dt>
<dd>Make <code>reloader</code> work on Windows. (tx manatlan)</dd>

<dd>Fix some small typos that affected colorization. (tx Gregory Price)</dd>

<dt>2006-01-03: 0.113</dt>
<dd>Reorganize <code>run()</code> internals so mod_python can be used. (tx Nicholas Matsakis)</dd>

<dt>2006-01-03: 0.112</dt>
<dd>Make <code>reloader</code> work when <code>code.py</code> is called with a full path. (tx David Terrell)</dd>

<dt>2006-01-03: 0.111</dt>
<dd>Fixed bug in <code>strips()</code>. (tx Michael Josephson)</dd>

<dt>2006-01-03: 0.11</dt>
<dd>First public version.</dd>
</dl>




























