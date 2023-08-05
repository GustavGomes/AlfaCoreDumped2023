
using AlfaCoreDumped.Infrastructure.DbContext;
using Microsoft.EntityFrameworkCore;

namespace AlfaCoreDumped
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            var configuration = new ConfigurationBuilder()
                .AddJsonFile("appsettings.json");
            var config = configuration.Build();
            var connectionStringDb = config["ConnectionStringDb"];

            // Add services to the container.
            builder.Services.AddControllers()
                .AddNewtonsoftJson(options =>
                {
                    options.SerializerSettings.Converters
                        .Add(new Newtonsoft.Json.Converters.StringEnumConverter());
                    options.SerializerSettings.TypeNameHandling = Newtonsoft.Json.TypeNameHandling.None;
                });

            // Create the context with a MySql Db
            builder.Services.AddDbContext<AlfaDbContext>(dbContextOptions =>
                dbContextOptions.UseMySql(connectionStringDb, new MySqlServerVersion(new Version(8, 0, 29))));


            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            app.UseHttpsRedirection();

            app.UseAuthorization();

            app.MapControllers();

            app.Run();
        }
    }
}