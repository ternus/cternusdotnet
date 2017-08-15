require "rubygems"

target_user     = "ternus"
target_host     = "cternus.net"
target_dir      = "/var/www/cternus.net"

public_dir      = "public"    # compiled site directory
source_dir      = "content"    # source file directory
static_dir      = "static"
posts_dir       = "posts"    # directory for blog files
new_post_ext    = "markdown"  # default new post file extension when using the new_post task

desc "build site"
task :build do
  sh "hugo"
end

desc "deploy site"
task :deploy do
  sh "rsync -Pav #{public_dir}/ #{target_user}@#{target_host}:#{target_dir}"
end

desc "Begin a new post in #{source_dir}/#{posts_dir}"
task :new_post, :title do |t, args|
  if args.title
    title = args.title
  else
    title = get_stdin("Enter a title for your post: ")
  end
  raise "### You haven't set anything up yet. First run `rake install` to set up an Octopress theme." unless File.directory?(source_dir)
  mkdir_p "#{source_dir}/#{posts_dir}"
  filename = "#{source_dir}/#{posts_dir}/#{Time.now.strftime('%Y-%m-%d')}-#{to_url(title)}.#{new_post_ext}"
  if File.exist?(filename)
    abort("rake aborted!") if ask("#{filename} already exists. Do you want to overwrite?", ['y', 'n']) == 'n'
  end
  puts "Creating new post: #{filename}"
  open(filename, 'w') do |post|
    post.puts "---"
    post.puts "title: \"#{title.gsub(/&/,'&amp;')}\""
    post.puts "date: #{Time.now.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    post.puts "draft: true"
    post.puts "url: /blog/#{Time.now.strftime('%Y/%m/%d/')}#{to_url(title)}/"
    post.puts "categories: []"
    post.puts "---"
  end
end


def to_url(title)
  title.downcase.gsub(/[^\w]/, '-')
end

def get_stdin(message)
  print message
  STDIN.gets.chomp
end

def ask(message, valid_options)
  if valid_options
    answer = get_stdin("#{message} #{valid_options.to_s.gsub(/"/, '').gsub(/, /,'/')} ") while !valid_options.include?(answer)
  else
    answer = get_stdin(message)
  end
  answer
end

desc "list tasks"
task :list do
  puts "Tasks: #{(Rake::Task.tasks - [Rake::Task[:list]]).join(', ')}"
  puts "(type rake -T for more detail)\n\n"
end
